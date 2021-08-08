import os
import random

f = open('flag-decs2.png', 'rb')
data = bytearray(f.read())
f.close()

k = 0.1

for i in range(0x123, len(data) - 8):
    if sum([data[i - 3] == 0x49, data[i - 2] == 0x44, data[i - 1] == 0x41, data[i] == 0x54]) > 1:
        data[i - 3] = 0x49
        data[i - 2] = 0x44
        data[i - 1] = 0x41
        data[i    ] = 0x54

f = open('flag-decs3.png', 'wb')
f.write(data[:0x129] + data[-8:])
f.close()