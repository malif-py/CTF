flag = 'picoCTF{16_bits_inst34d_of_8_75d4898b}'
res = ''
for i in range(0, len(flag), 2):
    arg1 = ord(flag[i]) << 8 
    arg2 = ord(flag[i + 1])
    argres = (arg1 + arg2)
    print(chr(argres), end='')