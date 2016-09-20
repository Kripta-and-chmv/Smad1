import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import Functions as f


N = 25
p = 0.08
w2 = .0
dispers = .0
U = np.zeros(N)
y = np.zeros(N)
t = .0
x1 = np.random.uniform(-1, 1, N)
x2 = np.random.uniform(-1, 1, N)

#def FindResponds(outputFile):
for i in range(N):
    #mean, U[i] = means(x1[i], 0, N, U)
    mean, U[i] = f.means(0, x2[i], N)
    tr = (U[i] - mean)
    w2 += tr.transpose() * (U[i] - mean)

w2 = w2 / (N - 1)
dispers = p * w2
ej = np.random.normal(0, dispers, N)

for i in range(N):
    y[i] = U[i] + ej[i]

names=['x1', 'x2']
seq = [x1, x2]
f.WritingInFile(names, seq, 'x1x2.txt')

#f.graph(x1, y)
f.graph(x2, y)