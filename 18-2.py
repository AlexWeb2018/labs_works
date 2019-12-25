import random
import numpy as np

M = random.randrange(2,7)
N = random.randrange(2,7)
K = random.randrange(0,M)
print("M = ",M,"; N = ",N,"; K = ",K)
a = np.zeros((M, N))

for i in range(M):
    for j in range(N):
        a[i][j] = random.randrange(1,5)
print(a)

Sum = sum(a[K])
Product = np.product(a[K])
print(a[K])
print("Sum: ",Sum)
print("Product: ",Product)