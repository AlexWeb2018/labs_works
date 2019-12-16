import random

N = random.randrange(2,21)
print("N = ", N)

a = [random.randrange(1,21) for i in range(N)]

##for i in range(0,N):
##    a[i] = i

print(a)

flag = False
for i in range(N-2,0,-1):
    print(i)
    if a[i-1] < a[i] and a[i] > a[i+1]:
        flag = True
        break
if flag:
    print("Index of Last Local maximum:",i)