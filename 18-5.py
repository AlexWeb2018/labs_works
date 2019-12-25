import random
import numpy as np

M = random.randrange(2,8)
N = random.randrange(2,8)
print("M = ",M,"; N = ",N)
a = np.random.randint(5, size=(M, N))
print(a)

print()
