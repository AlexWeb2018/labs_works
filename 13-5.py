import random

N = random.randint(10,20)
#N = 17
print("N = ", N)

L1 = [random.randint(1,10) for i in range(N)]
print("Initial:")
print(L1)

print("Odd indices:")
print(L1[1::2])    
L3 = [j for i, j in enumerate(L1) if i%2 == 1]
print(L3)

print("Even indices:")
x = int((N-1)/2)*2 + 1
L1_1 = L1[0:x]
print((L1_1)[::-2])    
L2 = [j for i, j in enumerate(L1) if i%2 == 0]
print(L2[::-1])