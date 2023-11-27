import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

with open('large.txt') as file:
    N = int(file.readline())
    data = np.loadtxt(file.readlines())
    A, B = np.array_split(data, [N], axis=0)
    B = np.transpose(B)

X = np.transpose(sp.linalg.solve(A, B))[0]

plt.bar(np.arange(N), X)
plt.savefig('matrix.png')
plt.show()
