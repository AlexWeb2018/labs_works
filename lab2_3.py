import random

#A,C,B = sorted(random.sample(range(-10, 10), 3))
a = int(input());
c = int(input());
b = int(input());
print("A: ", a)
print("B: ", b)
print("C: ", c)
ac = abs(a-c)
bc = abs(b-c)
ac_bc = ac * bc
print("AC: ", ac)
print("BC: ", bc)
print("AC * BC: ", ac_bc)
