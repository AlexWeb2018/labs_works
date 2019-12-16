import random

N = random.randrange(2,21)
a = [random.randrange(0,5) for i in range(N)]

print("N = ", N)
print("Array:\n",a)

i = 0
while i < len(a) :
    x = a[i]
    k = 0
    for y in a :
        if x == y :
            k += 1
    if k == 2 :
        flag = True
        while flag :
            try:
                a.remove(x)
            except ValueError:
                flag = False
    else :
        i += 1
        

print("Modified Array:\n",a)
print("Length:\n",len(a))