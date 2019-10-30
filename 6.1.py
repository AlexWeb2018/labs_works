import random

N = int(input("Введите число секунд: "))
print("Число секунд: ", N)
m = int(N / 60)
print("Число полных минут: ", m)
m = m % 60
print("Минуты с последнего часа: ", m)