import random
import math

N = random.randrange(2,15)
A = random.randrange(-5,5)
B = random.randrange(-5,5)
print("N = ", N)
print("A = ", A)
print("B = ", B)

a = [A,B]
for i in range(2,N):
    x = a[i-2] + a[i-1]
    a.append(x)
print(a)