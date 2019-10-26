import random

N = int(input("Введите число: "))
d2 = int(N / 100)
d1 = int((N - d2 * 100) / 10)
d0 = N % 10
print("Сотни: ", d2)
print("Десятки: ", d1)
print("Единицы: ", d0)
print("Другое число: ", d1 * 100 + d0 * 10 + d2)