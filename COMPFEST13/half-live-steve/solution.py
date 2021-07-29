import sympy
import time
start_time = time.time()
def fun1(x):
    # x // [i for i in range(1, x + 1) if x % i == 0][1]
    i = 1 
    q = sympy.prime(i)
    while x % q != 0:
        i += 1
        q = sympy.nextprime(q)
    return x // q
def parent_fun(x):
    if x == 1 or sympy.isprime(x):
        return False
    else:
        return sympy.isprime(fun1(x))
def res(start, n_start, n_end):
    distance = n_end - n_start
    i = start
    while distance != 0:
        i += 1 if distance > 0 else -1
        if parent_fun(i):
            distance -= (1 if distance > 0 else -1)
    return i

part1 = [93, 380, 529, 808, 1028, 1307, 1443, 1645, 1750, 2035, 2198, 2308, 2592, 5431, 7221, 9553, 11449, 13429, 15359, 18268, 20677, 22690, 24310, 26342, 28561, 53607, 65550, 90362, 112012, 124846, 149572, 167415, 179176, 192577, 202971, 226896, 238931, 238927, 400885, 400882, 400886, 400881, 400880, 400878, 400881, 400888, 400887, 400885, 400884, 400878, 400878]
part2 = [361, 1346, 1891, 2819, 3641, 4830, 5354, 6038, 6491, 7678, 8258, 8597, 9926, 21419, 28968, 38992, 46992, 55790, 64359, 77179, 87908, 96952, 104085, 113381, 123382, 239010, 295104, 413285, 517955, 580204, 700856, 788889, 847166, 913771, 965098, 1084194, 1144811, 1144617, 1967166, 1967140, 1967123, 1967205, 1967177, 1967172, 1967189, 1967119, 1967109, 1967167, 1967136, 1967107, 1967179]

strt = 4
n_strt = 1

for i in range(len(part1)):
    key = res(strt, n_strt, part1[i])
    print(chr(part2[i] ^ key), end='', flush=True)

    strt = key
    n_strt = part1[i]

print("\n----- %s seconds -----" % (time.time() - start_time))