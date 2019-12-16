import random

N = random.randrange(2,11)
a = random.sample(range(0, 100), N)
i = random.randrange(0,N)
a.append(a[i])
random.shuffle(a)

print("N:",N)
print("Array:\n",a)

flag = False
for i in range(0,N-1) :
    for j in range(i+1,N) :
        #print(i,":",j)
        if a[i] == a[j] :
            flag = True
            break
    if flag :
        break

print("Indices:", i,",",j)
