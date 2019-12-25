1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
from random import random
 
N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
a = []
for i in range(N):
    z = []
    for j in range(M):
        n = int(random() * 50) - 25
        z.append(n)
        print("%4d" % n, end='')
    print()
    a.append(z)
print()
 
k = M-1
while k > 0:
    ind = 0
    for i in range(k+1):
        if a[0][i] > a[0][ind]:
            ind = i
    for j in range(N):
        m = a[j][ind]
        a[j][ind] = a[j][k]
        a[j][k] = m
    k -= 1
 
for i in range(N):
    for j in range(M):
        print("%4d" % a[i][j], end='')
    print()