import random

N = random.randrange(2,21)
a = [random.randrange(1,50) for i in range(N)]
##N = 6
##a = [30, 21, 17, 1, 6, 39]
##N = 15
##a = [42, 17, 43, 3, 35, 32, 5, 31, 37, 9, 17, 41, 18, 42, 10]

print("N = ", N)
print("Array:\n",a)

max_val = max(a)
max_idx = a.index(max_val)

min_val = min(a)
min_idx = a.index(min_val)

print("Max:",max_val,"; Index:",max_idx)
print("Min:",min_val,"; Index:",min_idx)

if min_idx < max_idx :    
    print("Modified Array 1:\n",a[:min_idx] + [0] + a[min_idx:max_idx+1] + [0] + a[max_idx+1:])
else :
    print("Modified Array 1:\n",a[:max_idx+1] + [0] + a[max_idx+1:min_idx] + [0] + a[min_idx:])
    
if min_idx < max_idx :    
    K = min_idx
    a.append(-999)
    for i in range(N,K,-1) :
        a[i] = a[i-1]
    a[K] = 0
    
    K = max_idx
    a.append(-999)
    for i in range(N+1,K+2,-1) :
        a[i] = a[i-1]
    a[K+2] = 0
else :
    K = max_idx
    a.append(-999)
    for i in range(N,K,-1) :
        a[i] = a[i-1]
    a[K+1] = 0
    
    K = min_idx
    a.append(-999)
    for i in range(N+1,K+1,-1) :
        a[i] = a[i-1]
    a[K+1] = 0

print("Modified Array 2:\n",a)
print("Length:\n",len(a))