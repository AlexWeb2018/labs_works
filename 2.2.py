0import random

A,C,B = sorted(random.sample(range(-10, 10), 3))

print("A: ", A)
print("B: ", B)
print("C: ", C)
AC = abs(A-C)
BC = abs(B-C)
AC_BC = AC + BC
AB = abs(A-B)
print("AC: ", AC)
print("BC: ", BC)
print("AC + BC: ", AC_BC)
print("AB: ", AB)