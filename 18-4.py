import random
import numpy as np

M = random.randrange(2,8)
N = random.randrange(2,8)
print("M = ",M,"; N = ",N)
a = np.random.randint(5, size=(M, N))
print(a)

print()
for j in range(N):
    x = a[:,j]
    x_mean = np.mean(x)
    c = sum(item > x_mean for item in x)
    print("Column:",x)
    print("Mean:",x_mean)
    print("Number of items > Mean:",c)
    print()