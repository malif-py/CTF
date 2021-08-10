from pwn import *

r = remote('mercury.picoctf.net', 28517)

data = r.recvlines(4)
n = int(str(r.recvline())[5:-3])
e = int(str(r.recvline())[5:-3])
c = int(str(r.recvline())[13:-3])
i = bytes(str(c * (n + 1)), 'utf-8')
r.sendline(i)
data = str(hex(int(str(r.recvlines(3)[-1])[46:-1])))[2:]
res = "".join([chr(int(data[i - 1:i + 1], 16)) for i in range(1, len(data), 2)])
print(res)