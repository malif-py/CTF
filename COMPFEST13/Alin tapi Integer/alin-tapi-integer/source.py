import random
import numpy as np

m = np.array([int(open("s1.txt", "r").read()), int(open("s2.txt", "r").read())])
r = np.array([[random.getrandbits(100), random.getrandbits(100)], [random.getrandbits(100), random.getrandbits(100)]])
e = np.array([random.getrandbits(100), random.getrandbits(100)])

c = np.dot(r, e) + m
d = np.dot([r[0][1], r[1][1]], e) + m

print("r = {}".format(r))
print("c = {}".format(c))
print("d = {}".format(d))