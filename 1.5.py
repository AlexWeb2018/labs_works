# Даны два ненулевых числа. Найти сумму, разность, произведение и
# частное их модулей

# Даны два ненулевых числа. Найти сумму, разность, произведение и
# частное их квадратов


import math

a = int(input());
b = int(input());

# модуль
a = math.fabs(a);
b = math.fabs(b);

# сумма

sm = a + b;

# разность

raz = a - b;

# произведение

pr = a * b;

# частное

cst = a / b;

print(sm);
print(raz);
print(pr);
print(cst);