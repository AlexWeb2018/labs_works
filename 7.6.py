a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))


if ((a * a == b * b + c * c) or (b * b == a * a + c * c) or (c * c == b * b + a * a)):
	print("Треугольник является прямоугольным")
else:
	print("Треугольник не является прямоугольным")