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

def WritingInFile(names, sequences, fileName):
    with open(fileName, 'w') as f:
        for i in range(len(names)):
            f.write(names[i] + ':\n')
            for j in range(len(sequences[i])):
                f.write('\t' + str(sequences[i][j]) + '\n')