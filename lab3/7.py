# Дано число A. Вычислить A15, используя две вспомогательные
# переменные и пять операций умножения.





import random

A = int(input())
A = 2
print("A = ",A)
x = A * A
print("A^2 = ",x)
A = x * A
print("A^3 = ",A)
A = x * A
print("A^5 = ",A)
x = A * A
print("A^10 = ",x)
A = x * A
print("A^15 = ",A)