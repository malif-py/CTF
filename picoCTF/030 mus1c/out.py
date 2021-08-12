f = open("converted.txt")
for i in f:
    print(chr(int(i)), end='')