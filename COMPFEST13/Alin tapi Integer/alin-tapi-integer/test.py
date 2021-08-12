from math import gcd, lcm
import random
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy.assumptions.ask import Q
c_1 = 488768506535711467631486121787661988127930750854331538644781
c_2 = 547482607752108045694137599846025101796395117165560647421809
r_0_0 = 495916083754780757592152695841
r_0_1 = 470498165644937909945089827048
r_1_0 = 51409727317788514842675159705
r_1_1 = 974977445722134917915952509711
kiri  = [c_1 // r_0_0,
         c_1 // r_1_0]
kanan = [c_2 // r_0_1,
         c_2 // r_1_1]
mat = np.array([kanan, kiri], dtype='float')
resl = np.array([kanan[0] * kanan[1], kiri[0] * kiri[1]])
res = np.matmul(np.linalg.inv(mat), resl)
tengah = [int(res[1]), int(res[0])]
kiri_0   = [c_1, c_2] - np.dot([kiri[0],   0], [[r_0_0, r_0_1], [r_1_0, r_1_1]])
kanan_1  = [c_1, c_2] - np.dot([0,  kanan[1]], [[r_0_0, r_0_1], [r_1_0, r_1_1]])
tengah_0 = [c_1, c_2] - np.dot(tengah, [[r_0_0, r_0_1], [r_1_0, r_1_1]])

print(np.dot(tengah, [r_0_1, r_1_1]) > c_2)