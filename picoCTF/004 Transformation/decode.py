encoded = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'
flag = ''

for i in encoded:
    raw = ord(i)
    txt1 = raw // 2 ** 8
    txt2 = raw - txt1 * 2 ** 8
    flag = flag + chr(txt1) + chr(txt2)

print(flag)