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
            arr[i] = [arr[i + 1].split(',')]
            arr[i + 1] = ''
        elif arr[i] == 'Q':
            arr[i] = [arr[i + 1].split(','), arr[i + 2].split(',')]
            arr[i + 1] = ''
            arr[i + 2] = ''
        elif arr[i] == 'C':
            arr[i] = [arr[i + 1].split(','), arr[i + 2].split(','), arr[i + 3].split(',')]
            arr[i + 1] = ''
            arr[i + 2] = '' 
            arr[i + 3] = ''
        elif arr[i] == 'V'  or arr[i] == 'H':
            arr[i] = ''
            arr[i + 1] = ''
        elif arr[i] == 'L':
            arr[i + 1] = [arr[i + 1].split(',')]
    
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
                if arr[1 + i][j][k] != '?' and arr[1 + i][j][k] != 'Z' and arr[1 + i][j][k] != 'L' :
                    arr[1 + i][j][k] = float(arr[1 + i][j][k])
def solve(m, q, c):
    con = list(q + c)
    for i in range(len(con)):
        con[i] = con[i][0] != '?'
    while not all(con):
        if con[1]:
            con[4] = con[1]
            c[2] = q[1]
        if con[4]:
            con[1] = con[4]
            q[1] = c[2]
        if con[0]:
            if not con[2]:
                # C Control Point 1
                c[0][0] = m[0][0] + 2 / 3 * (q[0][0] - m[0][0])
                c[0][1] = m[0][1] + 2 / 3 * (q[0][1] - m[0][1])
            if not con[3]:
                # C Control Point 2
                c[1][0] = q[1][0] + 2 / 3 * (q[0][0] - q[1][0])
                c[1][1] = m[0][1] + 2 / 3 * (q[0][0] - q[1][1])
        else:
            if con[2]:
                q[0][0] = 3 / 2 * (c[0][0] - 1 / 3 * m[0][0])
                q[0][1] = 3 / 2 * (c[0][1] - 1 / 3 * m[0][1])
            if con[3] and con[4]:
                q[0][0] = 3 / 2 * (c[1][0] - 1 / 3 * q[1][0])
                q[0][1] = 3 / 2 * (c[1][1] - 1 / 3 * q[1][1])
        if q[0][0] != '?' and c[1][0] != '?':
            q[1][0] = 3 * (c[1][0] - 2 / 3 * q[0][0])
            q[1][1] = 3 * (c[1][1] - 2 / 3 * q[0][1])
        con = list(q + c)
        for i in range(len(con)):
            con[i] = con[i][0] != '?'
def line_solve(arr_q, arr_c):
    solve(arr_q[1],arr_q[2],arr_c[2])
    i = 0
    while i < len(arr_q[3:]):            
        if arr_q[2 + i] == 'Z':
            solve(arr_q[3 + i], arr_q[4 + i], arr_c[4 + i])
            i += 1
        elif arr_q[2 + i] == 'L':
            print(arr_q[3+i])
            print(arr_q[4+i])
            print(arr_c[4+i])
            solve(arr_q[3 + i], arr_q[4 + i], arr_c[4 + i])
            i += 1
        else:
            solve([arr_q[2 + i][1]], arr_q[3 + i], arr_c[3 + i])
        i += 1


text1 = open("missing_coor1.svg")
text2 = open("missing_coor2.svg")

ltot1 = text1.readlines()
ltot2 = text2.readlines()

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