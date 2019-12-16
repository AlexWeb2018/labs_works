import random

N = random.randrange(2,10)
a = [random.randrange(1,11) for i in range(N)]

print("N:",N)
print("Array a:\n",a)

x_odd = None
for i in range(N-1,-1,-1) :
    if a[i]%2 == 1 :
        x_odd = a[i]
        break
print("Last odd:",x_odd)

if x_odd != None :
    for (i, item) in enumerate(a) :
        if item%2 == 1:
            a[i] += x_odd

print("Modified Array a:\n",a)