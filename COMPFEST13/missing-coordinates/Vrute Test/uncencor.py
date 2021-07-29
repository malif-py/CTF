file = open("result.svg")
wr = open('heheh.svg', 'w')
kyun = file.readlines()
a = []
for i in kyun:
    if (i.strip()[:5]) == '<path' and len(i.strip()) >= 200:
        wr.write(i)
    elif (i.strip()[:5]) != '<path':
        wr.write(i)