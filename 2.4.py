import math

x1 = float(input("Введите x1 - "))

y1 = float(input("Введите y1 - "))

x2 = float(input("Введите x2 - "))

y2 = float(input("Введите y2 - "))

X = abs(x2 - x1)
Y = abs(y1 - y2)

P = 2*(X + Y)
S = X * Y

print(P)
print(S)