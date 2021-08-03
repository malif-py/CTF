import random
random.seed("wadidaw")

enc_r = '1a 1a 31 63 de 16 00 f4 e4 22 39 dc 90 d9 9e 5a 29 ed 49 f0 80 a2 0d 20 79 4e f8 b2 0a'.split(' ')
enc_p = [int(i, 16) for i in enc_r]
randm = [(random.randint(0x00, 0xFF),random.randint(0x00, 0xFF)) for i in enc_p]
text = ''
for i in range(len(enc_p)):
    out = enc_p[i] - randm[i][1]
    while out <= 0:
        out += 255
    out = out ^ randm[i][0]
    text += chr(out)

print(text)