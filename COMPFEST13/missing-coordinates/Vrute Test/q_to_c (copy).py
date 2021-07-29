from os import read


def parse_str(txt):
    i = len(txt)
    while txt[i - 1] != 'd':
        i -= 1
    k = len(txt)
    while txt[k - 1] != 'Z':
        k -= 1
    if txt[:9] == '<path d="':
        return (txt[i + 2:-4] + ' ' + txt[9:k]).split(' ')
    else:
        return (txt[i + 2:-3] + ' ' + txt[52:k]).split(' ')
def parse_arr(arr):
    for i in range(len(arr)):
        if arr[i] == 'M':
            arr[i] = [arr[i], arr[i + 1].split(',')]
            arr[i + 1] = ''
        elif arr[i] == 'Q':
            arr[i] = [arr[i], arr[i + 1].split(','), arr[i + 2].split(',')]
            arr[i + 1] = ''
            arr[i + 2] = ''
        elif arr[i] == 'C':
            arr[i] = [arr[i], arr[i + 1].split(','), arr[i + 2].split(','), arr[i + 3].split(',')]
            arr[i + 1] = ''
            arr[i + 2] = '' 
            arr[i + 3] = ''
        elif arr[i] == 'V':
            arr[i] = 'L'
            arr[i] = [arr[i], ['0', arr[i + 1]]]
            arr[i + 1] = ''
        elif arr[i] == 'H':
            arr[i] = 'L'
            arr[i] = [arr[i], [arr[i + 1], '0']]
            arr[i + 1] = ''
        elif arr[i] == 'L':
            arr[i] = [arr[i], arr[i + 1].split(',')]
            arr[i + 1] = ''
        elif arr[i] == 'Z':
            arr[i] = [arr[i]]
    
    res = []
    for l in arr:
        if l != '':
            res = res + [l]
    
    return res
def parse_full(txt):
    return parse_arr(parse_str(txt))
def atf(arr):
    for i in range(len(arr[1:])):
        for j in range(len(arr[1 + i])):
            for k in range(len(arr[1 + i][j])):
                if arr[1 + i][j][k] not in ['M', 'L', 'Q', 'C', 'Z', '?']:
                    arr[1 + i][j][k] = float(arr[1 + i][j][k])
def solve(m, q, c):
    con = list(q + c)
    for i in range(len(con)):
        if con[i] not in ['M', 'L', 'Q', 'C', 'Z']:
            con[i] = con[i][0] != '?'
    while not all(con):
        if con[2]:
            con[6] = con[2]
            c[3] = q[2]
        if con[6]:
            con[2] = con[6]
            q[2] = c[3]
        if con[1]:
            if not con[4]:
                # C Control Point 1
                c[1][0] = round(m[1][0] + 2 / 3 * (q[1][0] - m[1][0]), 2)
                c[1][1] = round(m[1][1] + 2 / 3 * (q[1][1] - m[1][1]), 2)
            if not con[5]:
                # C Control Point 2
                c[2][0] = round(q[2][0] + 2 / 3 * (q[1][0] - q[2][0]), 2)
                c[2][1] = round(q[2][1] + 2 / 3 * (q[1][1] - q[2][1]), 2)
        else:
            if con[4]:
                q[1][0] = round(3 / 2 * (c[1][0] - 1 / 3 * m[1][0]), 2)
                q[1][1] = round(3 / 2 * (c[1][1] - 1 / 3 * m[1][1]), 2)
            if con[5] and (con[6] or con[2]):
                q[1][0] = round(3 / 2 * (c[2][0] - 1 / 3 * q[2][0]), 2)
                q[1][1] = round(3 / 2 * (c[2][1] - 1 / 3 * q[2][1]), 2)
        if not con[2]:
            q[2][0] = round(3 * (c[2][0] - 2 / 3 * q[1][0]), 2)
            q[2][1] = round(3 * (c[2][1] - 2 / 3 * q[1][1]), 2)
        con = list(q + c)
        for i in range(len(con)):
            if con[i] not in ['M', 'L', 'Q', 'C', 'Z']:
                con[i] = con[i][0] != '?'
def line_solve(arr_q, arr_c):
    i = 0
    while i < len(arr_q[2:]):
        if arr_q[1 + i][0] == 'M' or arr_q[1 + i][0] == 'L':
            solve(arr_q[1 + i], arr_q[2 + i], arr_c[2 + i])
        else:
            solve(arr_q[1 + i], arr_q[2 + i], arr_c[2 + i])
        i += 1
def tostr(line):
    for i in range(len(line[1:])):
        for k in range(len(line[1 + i][1:])):
            line[1 + i][1 + k][0] = str(line[1 + i][1 + k][0])
            line[1 + i][1 + k][1] = str(line[1 + i][1 + k][1])
            line[1 + i][1 + k] = ','.join(line[1 + i][1 + k])
        line[1 + i] = ' '.join(line[1 + i])

text1 = open("missing_coor1.svg")
text2 = open("missing_coor2.svg")
resul = open("result.svg", 'w')

ltot1 = text1.readlines()
ltot1_clone = list(ltot1)
ltot2 = text2.readlines()
ltot2_clone = list(ltot2)

for i in range(len(ltot1)):
    if ltot1[i].strip()[:5] == '<path':
        ltot1[i] = parse_full(ltot1[i].strip())
        atf(ltot1[i])
    if ltot2[i].strip()[:5] == '<path':
        ltot2[i] = parse_full(ltot2[i].strip())
        atf(ltot2[i])

for i in range(len(ltot1)):
    if ltot1[i][0][:4] == 'path' and len(ltot1[i]) > 3:
        for k in range(len(ltot2)):
            if ltot1[i][0] == ltot2[k][0]:
                line_solve(ltot1[i][:-1],ltot2[k][:-1])

for i in range(len(ltot2)):
    if ltot2[i][0][:4] == 'path':
        tostr(ltot2[i])
        '''for k in range(len(ltot2[i])):
            if ltot2[i][k][0] == 'L':
                ltot2[i][k] = '''
        ltot2[i] = ' '.join(ltot2[i][1:])
        index_M = 0
        while ltot2_clone[i][index_M] != 'M':
            index_M += 1
        index_Z = len(ltot2_clone[i])
        while ltot2_clone[i][index_Z - 1] != 'Z':
            index_Z -= 1
        ltot2[i] = ltot2_clone[i][:index_M]+ ltot2[i] + ltot2_clone[i][index_Z:]

for i in ltot2:
    resul.write(i)