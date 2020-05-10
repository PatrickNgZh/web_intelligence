# Q1 b
import numpy as np

ATD = [[0, 0.5, 0.5],
       [0.5, 0, 0.5],
       [0.5, 0.5, 0]]

ce = [1 / 3, 1 / 3, 1 / 3]

ATD = np.array(ATD)
ce = np.array(ce).T
print(ATD)
print(ce)
print('======================================================')

n = 20
for i in range(n):
    ce = ATD @ ce
    print('Iteration' + str(i + 1), ':', ce)

