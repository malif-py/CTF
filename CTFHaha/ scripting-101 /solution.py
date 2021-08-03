# Import the pwntools library
# You can install this via pip install pwntools
from pwn import *

# To process local files
# r = process('./filename')

# To connect to a remote server via nc
r = remote('18.142.96.226', 10075)

# To receive a line of data (until it finds \n)
data = r.recvline()
data = str(r.recv())[2:-1]
while data[:3] != 'CTF':
    data_p = data.strip().split(' ')
    p1 = int(data_p[0])
    p2 = int(data_p[2])
    op = data_p[1]

    if op == '+':
        answer = p1 + p2
    elif op == '-':
        answer = p1 - p2
    elif op == "*":
        answer = p1 * p2
    answer = str(answer)
    answer = bytes(answer, 'utf-8')
    # To send input '1337' to the remote server
    r.sendline(answer)
    data = str(r.recv())[2:-1]
print(data)