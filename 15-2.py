import random

N = random.randrange(2,21)
#a = [random.randrange(1,11) for i in range(N)]
a = [i for i in range(N)]
b = []
c = []
b.append(a[0])
c.append(a[0])

print("N:",N)
print("Array a:\n",a)

for i in range(1,N) :
    b.append((a[i] + b[i-1]*i)/(i+1))
    c.append(a[i] + c[i-1])

print("Length of b:\n",len(b))
print("Array b:\n",b)
print("Array c:\n",c)