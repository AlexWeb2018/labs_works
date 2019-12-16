# Дано целое число N (> 0). 
# Найти произведение 1.1 · 1.2 · 1.3 
# · . . . (N сомножителей).


import random

N = random.randrange(1,15)
print('N = ', N)

S = 0.0
for i in range(1,N+1):
    x = (1 + i * 0.1) * (-1) ** (i+1)
    S += x
    print(i," : ",x," : ",S)
print("Sum = ",S)