import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

enc = 'ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih'

def unshift(alp, key):
    num = ord(alp) - LOWERCASE_OFFSET
    t2  = ord(key) - LOWERCASE_OFFSET
    return ALPHABET[(num - t2) % 16]

def b16_decode(msg):
    text = ''
    for i in range(0, len(msg), 2):
        bin1 = "{0:08b}".format(ord(msg[i]) - LOWERCASE_OFFSET)[4:]
        bin2 = "{0:08b}".format(ord(msg[i + 1]) - LOWERCASE_OFFSET)[4:]
        text += chr(int(bin1 + bin2, 2))
    return text

# Brute Force
for key in ALPHABET:
    msg = ''
    for i in enc:
        msg += unshift(i, key)
    print(b16_decode(msg))