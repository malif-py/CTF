import random

p = '[?] Plainteks: '
c = '[?] Cipherteks: '
k = '[?] Kunci: '

# https://stackoverflow.com/questions/43656104/creation-of-nxn-matrix-sudoku-like
def bitcount(n):
  i = 0
  while n:
    i += 1
    n &= n-1
  return i
def complete(S, rowset, colset, entries, seed):
  random.seed(seed)
  N = len(S)
  if entries == N * N:
    return True
  i, j = max(
    ((i, j) for i in xrange(N) for j in xrange(N) if S[i][j] == 0),
    key=(lambda (i, j): bitcount(rowset[i]|colset[j])))
  bits = rowset[i]|colset[j]
  p = [n for n in xrange(1, N+1) if not (bits >> (n-1)) & 1]
  random.shuffle(p)
  for n in p:
    S[i][j] = n
    rowset[i] |= 1 << (n-1)
    colset[j] |= 1 << (n-1)
    if complete(S, rowset, colset, entries+1, seed): return True
    rowset[i] &= ~(1 << (n-1))
    colset[j] &= ~(1 << (n-1))
  S[i][j] = 0
  return False

y = 65
r = []
N = 26
S = [[0] * N for _ in xrange(N)]
opt = int(raw_input('[*] Arkavidia Cipher\n\n[1] Enkrispi\n[2] Dekrispi\n\n[?] Opsi: '))
print ''
t = raw_input(p if opt == 1 else c)
q = raw_input(k)
q = ''.join(c for c in q if c.isalpha())
assert complete(S, [0]*N, [0]*N, 0, q)
i = 0
for ch in t:
  if ch.isalpha():
    if opt == 1: r.append(chr(S[ord(q[i%len(q)].upper())-y][ord(ch.upper())-y]+y-opt))
    else: r.append('*') # TU-DU: implement dekrispi
    i += 1
  else: r.append(ch)

print ''.join(r)