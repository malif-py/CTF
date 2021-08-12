import numpy as np

a1 = np.array([[1,2],[3,4]])
c1 = np.array([7, 8])
b1 = np.matmul(np.linalg.inv(a1), c1)
print(b1)