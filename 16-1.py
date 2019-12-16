import random

def RemoveDuplicate(i,A) :
    N = len(A) - 1
    while i < N :
        if A[i] == A[i+1] :
            A.pop(i+1)
            break
        else :
            i += 1
    return i
    

N = random.randrange(2,21)
a = [random.randrange(0,4) for i in range(N)]

print("N = ", N)
print("Array:\n",a)

flag = True
i = 0
while i < N-1:
    i = RemoveDuplicate(i,a)
    N = len(a)

print("Modified Array:\n",a)
print("Length:\n",len(a))