#Traceback (most recent call last):
# File "main.py", line 5, in <module>
#   a = int(input("введите " + n + " координаты 1-ой точки: "));
#ValueError: invalid literal for int() with base 10: '3 4'


import math
 #задать количество точек для одной переменной
n = input("Количество измерений пространства: ")
print("Через пробел")
a = int(input("введите " + n + " координаты 1-ой точки: "));
b = int(input("введите " + n + " координаты 2-ой точки: "));
n = int(n)
#разделить числа
a = a.split()
b = b.split()

#проверка на правильность ввода
if len(a) != n or len(b) != n: 
	print("Неверный ввод!")
	exit()
 
sum_sqr = 0
for i, j in zip(a,b):
	sum_sqr += (int(i)-int(j))**2
distance = math.sqrt(sum_sqr)


pr = 2(a * b);
s = a * b;
