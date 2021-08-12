#!/usr/bin/python3
import sys
from binascii import hexlify, unhexlify
from os import urandom
from Crypto.Util.number import long_to_bytes as lb, bytes_to_long as bl
from secret import flag


KEYS = None


bytn = lambda x, n: (x >> (n * 8)) & 0xff
bitn = lambda x, n: (x >> n) & 0x1
shift = lambda x: ((x << 2) | (x >> 6)) & 0xff
add_n_shift = lambda x, y, z: shift((x + y + z) % 0x100)


class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)


def scramble(inp, key):
    temp = bytn(inp, 1) ^ bytn(key, 1) ^ bytn(inp, 0)
    out_2 = add_n_shift(bytn(inp, 2) ^ bytn(key, 2) ^ bytn(inp, 3), temp, 1)
    out_1 = add_n_shift(temp, out_2, 0)
    out_0 = add_n_shift(bytn(inp, 0) ^ bytn(key, 0), out_1, 1)
    out_3 = add_n_shift(bytn(inp, 3) ^ bytn(key, 3), out_2, 0)
    return ((out_3 << 24) | (out_2 << 16) | (out_1 << 8) | (out_0))


def sub_encrypt(pt, keys):
    key_1, key_2, key_3, key_4, key_5, key_6 = keys
    ls, rs = pt >> 32 & 0xffffffff, pt & 0xffffffff

    # initialize
    ls, rs = ls, ls ^ rs
    # scramble part 1
    ls, rs = ls ^ scramble(rs, key_1), rs
    ls, rs = rs ^ scramble(ls, key_2), ls
    # mix key
    ls, rs = ls, rs ^ key_5
    ls, rs = rs, ls ^ key_6
    # scramble part 2
    ls, rs = ls ^ scramble(rs, key_3), rs
    ls, rs = rs ^ scramble(ls, key_4), ls
    # finalize
    ls, rs = ls, rs ^ ls

    assert ls < 2 ** 32
    assert rs < 2 ** 32
    return ((ls << 32) | (rs))


def encrypt(pt, keys):
    ct = b''
    for block in [pt[i:i+8] for i in range(0, len(pt), 8)]:
        ct += sub_encrypt(int.from_bytes(block, byteorder='big'), keys).to_bytes(length=8, byteorder='big')
    return ct


def decrypt(ct, keys):
    dec_keys = [keys[3], keys[2], keys[1], keys[0], keys[5], keys[4]]
    pt = b''
    for block in [ct[i:i+8] for i in range(0, len(ct), 8)]:
        pt += sub_encrypt(int.from_bytes(block, byteorder='big'), dec_keys).to_bytes(length=8, byteorder='big')
    return pt


def pad(pt):
    return pt + chr(8 - len(pt) % 8).encode() * (8 - len(pt) % 8)


def reset():
    global KEYS
    KEYS = [int.from_bytes(urandom(4), byteorder='big') for i in range(6)]
    id = hexlify(encrypt(pad(flag), KEYS))
    print(f'Your account id: {id}')
    assert flag.startswith(b'Arkav7')
    assert pad(flag) == decrypt(unhexlify(id), KEYS)


if __name__ == '__main__':
    print('Welcome to scramble machine...\n'
          '<Warning> You are using free account.')
    reset()
    counter = ord('\'')
    try:
        while counter:
            print('\n'
                  'Menu\n'
                  '1. Encrypt something\n'
                  '2. Decrypt something\n'
                  '3. Reset keys\n'
                  '4. Free account limitation\n'
                  '5. Exit')
            option = int(input('Input your choice: '))
            if option == 1:
                inp = unhexlify(input('Input your text (in hex): '))
                inp = pad(inp)[:8]
                print('Here is your signed input and the encrypted value:')
                for i in range(5):
                    signed_inp = lb(bl(inp) ^ (bl(urandom(4)) << (i * 8)))
                    print(f'({hexlify(signed_inp)}, {hexlify(encrypt(signed_inp, KEYS))})')
            elif option == 2:
                print('This feature is limited to premium account!')
            elif option == 3:
                reset()
            elif option == 4:
                print('- Can not use decrypt feature\n'
                      '- Maximum input length for encryption feature is 8 chars\n'
                      '- Input for encryption feature is signed using string of our choice')
            else:
                print('Thanks... Please consider upgrading your account...')
                exit(0)
            counter -= 1
    except Exception as e:
        print('Error happened...')
        exit(0)
