import random
import math

N = random.randrange(1,10)
A = random.randrange(-10,10)
D = round(random.randrange(-5,5),1)
print("N = ", N)
print("A = ", A)
print("D = ", D)

a1 = []
for i in range(N):
    x = A * (D**i)
    a1.append(x)
print(a1)

a2 = [A * (D**i) for i in range(N)]
print(a2)