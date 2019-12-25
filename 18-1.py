import random
import numpy

#M = random.randrange(2,10)
M = 9
print("M = ",M)
a = numpy.zeros((M, M))
#a.astype(int)

k = 0
for i in range(0,M):
    for j in range(i,M-i):
        k += 1
        a[j][i] = k

    for j in range(i+1,M-i):
        k += 1
        a[M-1-i][j] = k

    for j in range(M-2-i,i-1,-1):
        k += 1
        a[j][M-1-i] = k

    for j in range(M-2-i,i,-1):
        k += 1
        a[i][j] = k

    i +=2

print(a)


k = 0
for i in range(0,M):
    for j in range(i,M-i):
        print(a[j][i], end=" ")

    for j in range(i+1,M-i):
        print(a[M-1-i][j], end=" ")

    for j in range(M-2-i,i-1,-1):
        print(a[j][M-1-i], end=" ")

    for j in range(M-2-i,i,-1):
        print(a[i][j], end=" ")

    i +=2