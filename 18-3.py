import random
import numpy as np

M = random.randrange(2,8)
N = random.randrange(2,8)
print("M = ",M,"; N = ",N)
a = np.random.randint(5, size=(M, N))
print(a)

S = np.prod(a,axis=0)
print("\nProduct of columns:")
print(S)

S_max = max(S)
print("\nMaximum of products:",S_max)

idx = [i for i, x in enumerate(S) if x == S_max]
print("Indices of Max:",idx)