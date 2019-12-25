import random
s=0
i=0
k=1
N=int(input())
A=[[random.randrange(10) for i in range(N)] for j in range(N)]
for k in range(N):
    while i<N:
        while k<N:
            s+=A[i][k]
            k+=1
        i+=1
print(s)