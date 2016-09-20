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

def FindResponds(x1, x2, outputFile, N):
    p = 0.08
    w2 = .0
    dispers = .0
    U = np.zeros(N)
    y = np.zeros(N)
    t = .0

    for i in range(N):        
        mean, U[i] = means(x1[i], x2[i], N)
        tr = (U[i] - mean)
        w2 += tr.transpose() * (U[i] - mean)

    w2 = w2 / (N - 1)
    dispers = p * w2
    ej = np.random.normal(0, dispers, N)

    for i in range(N):
        y[i] = U[i] + ej[i]
    
    WritingInFile(['U', 'ej', 'y'], [U, y, ej], outputFile)

    return y
