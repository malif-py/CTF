from Crypto.Hash import MD5

def encrypt(plaintext):
    length = len(plaintext)
    left = plaintext[:length // 2]
    right = plaintext[length // 2:]
    keys = [line[:16] for line in open('keys.txt', 'rb').readlines()]
    ciphertext = b''
    for key in keys:
        assert len(key) == 16
        tmp = right
        right = xor(right, key)
        h = MD5.new()
        h.update(right)
        right = h.hexdigest().encode()
        left = xor(left, right)
        right = left
        left = tmp
    return right+left
        
def xor(a, b):
    ciphertext = b''
    l_a = len(a)
    l_b = len(b)
    for i in range(l_a):
        ciphertext += str(chr(a[i % l_a] ^ b[i % l_b])).encode()
    return ciphertext

flag = open('flag.txt', 'rb').read()
print(len(flag))
assert len(flag) == 32
encrypted = open('encrypted1.txt', 'wb')
encrypted.write(encrypt(flag))
