#  Даны переменные A, B, C. Изменить их значения, переместив
# содержимое A в C, C — в B, B — в A, и вывести новые значения переменных
# A, B, C.


import random

A = int(input())
B = int(input())
C = int(input())
print("A = {0}, B = {1}, C = {2}".format(A,B,C))

A,B = B,A
A,C = C,A
print("A = {0}, B = {1}, C = {2}".format(A,B,C))