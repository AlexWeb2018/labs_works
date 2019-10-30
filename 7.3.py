import random
A = int(input("Введите A: "))
a = (A % 2 == 0)
b = (A >= 10 and A <= 99)
x = (a and b)
print("A четно: ", a)
print("A двузначно: ", b)
print("Данное число является четным двузначным: ", x)