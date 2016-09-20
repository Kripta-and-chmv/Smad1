import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

def func(X, Y):
    return 1 + X - sp.exp(-X ** 2) + Y ** 2

def means(x, y, N):
    mean = .0
    f = func(x, y)
    for i in range(N):
        mean += f
    mean = mean / N
    return mean, f

def graph(x, y):
    p1 = plt.plot(x, y, 'ro')
    plt.show()

def WritingInFile(x1, x2, y, U, ej):
    with open('output.txt', 'w') as f:

        f.write('x1:\n')
        for i in range(len(x1)):
            f.write('\t' + str(x1[i]) + '\n')
        
        f.write('x2:\n')
        for i in range(len(x2)):
            f.write('\t' + str(x2[i]) + '\n')

        f.write('y:\n')
        for i in range(len(y)):
            f.write('\t' + str(y[i]) + '\n')

        f.write('U:\n')
        for i in range(len(U)):
            f.write('\t' + str(U[i]) + '\n')

        f.write('ej:\n')
        for i in range(len(ej)):
            f.write('\t' + str(ej[i]) + '\n')