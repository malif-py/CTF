from Crypto.Hash import MD5

def xor(a, b):
    ciphertext = b''
    l_a = len(a)
    l_b = len(b)
    for i in range(l_a):
        ciphertext += str(chr(a[i % l_a] ^ b[i % l_b])).encode()
    return ciphertext

def key_dcr(enc, key):
    left = enc[16:]
    rght = enc[:16]
    p_rght_p = xor(left, key)
    h = MD5.new()
    h.update(p_rght_p)
    p_rght_p = h.hexdigest().encode()
    p_left = xor(rght, p_rght_p)
    p_rght_r = left
    return p_rght_r + p_left

enc = b'klW~QV\nWHR\a<tq&9$v5eX=?Z@'
keys = [line[:16] for line in open('keys.txt', 'rb').readlines()][::-1]

for key in keys:
    enc = key_dcr(enc, key)

print(enc[16:] + enc[:16])