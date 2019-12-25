# Дано вещественное число A и целое число N (> 0). 
# Используя один цикл, найти значение выражения 
# 1 − A + A2 − A3 + . . . ± AN . 



N = int(input("N = "))
print('N = ', N)
A = int(input("A = "))
print('A = ', A)

P = 1.0
S = 1.0
for i in range(1, N + 1):
    P *= A * (-1)
    S += P
    print(i," : ", P," : ", S)
print("Result:",S)