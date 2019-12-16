import random

N = random.randrange(2,15)
a = random.sample(range(0, 100), N)
#a = [random.randrange(1,11) for i in range(N)]

print("N:",N)
print("Array a:\n",a)

max_val = max(a)
max_idx = a.index(max_val)

min_val = min(a)
min_idx = a.index(min_val)

print("Max:",max_val,"; Index:",max_idx)
print("Min:",min_val,"; Index:",min_idx)

if min_idx < max_idx :
    start_idx = min_idx
    end_idx = max_idx
else :
    start_idx = max_idx
    end_idx = min_idx

i = start_idx + 1
while i < end_idx :
    a[i] = 0
    i += 1

print("Modified Array a:\n",a)