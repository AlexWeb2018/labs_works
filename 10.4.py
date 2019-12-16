# Дано вещественное число A и целое число N (> 0). 
# Используя один цикл, найти сумму 1 + A + 
# A2 + A3 + . . . + AN


import random

N = int(input())
print('N = ', N)
A = int(input())
print('A = ', A)

P = 1.0
S = 1.0
for i in range(1 , N + 1):
    P *= A
    S += P
    print(i," : ", P," : ", S)
print("Result:",S)