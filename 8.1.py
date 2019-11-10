a = int(input("Введите a: "))
b = int(input("Введите b: "))

if (a == b):
	p = 0
else:
	p = a + b
	a = p
	b = p
	print('a = ', p, ', b = ', p)