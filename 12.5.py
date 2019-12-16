import random

def Fact2(N):
    F = 1.0
    while N > 0:
        F *= N
        N -= 2
    return F

for i in range(1,11):
    x = random.randrange(1,16)
    x = i
    print(x,":",Fact2(x))