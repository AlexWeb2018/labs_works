a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))


if ((a + b > c) and (b + c > a) and (c + a > b)):
	print("Треугольник существует")
else:
	print("Треугольник не существует")