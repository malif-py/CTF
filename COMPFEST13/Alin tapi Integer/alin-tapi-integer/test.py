import random
import numpy as np

m = np.array([int(open("s1.txt", "r").read()), int(open("s2.txt", "r").read())])
r = np.array([[1, 2], [3, 4]])
e = np.array([1, 2])

print(m)
print(r)
print(e)

c = np.dot(e, r)
print(c)
'''print("r = {}".format(r))
print("c = {}".format(c))'''