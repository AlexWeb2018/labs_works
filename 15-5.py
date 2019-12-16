import random

N = random.randrange(1,21)
##N = 1
a = [random.randrange(1,21) for i in range(N)]
a.sort()
x = random.randrange(a[0]+1,21)
a = [x] + a

print("N = ", N)
print("Array:\n",a)

K = 1
while K <= N and x > a[K] :
    K += 1
print("K:",K)

x = a[0]
for i in range(0,K-1) :
    a[i] = a[i+1]
a[K-1] = x
print("Modified Array:\n",a)