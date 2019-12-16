import random

N = random.randint(2,15)
K = int(N/2)
#N = 17
print("N = ", N)

L = [i+1 for i in range(N)]
print("Initial:")
print(L)

L1 = []
for i in range(0,K):
    L1.append(L[i])
    L1.append(L[N-1-i])
if 2*K < N:
    L1.append(L[K])
print(L1)