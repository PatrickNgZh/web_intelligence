import numpy as np

row, column = input().split(' ')

row = int(row)
column = int(column)
matrix = np.arange(row * column).reshape((row, column))

for i in range(int(row)):
    matrix[i] = input().split(' ')

values, vectors = np.linalg.eig(matrix)

print(np.around(values, decimals=3))

print(np.around(vectors, decimals=3))
