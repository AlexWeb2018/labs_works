a = int(input("Введите значение угла 0 < a < 360: "))
p = 3.14

if (a <= 0 or a >= 360):
	print("Не то число")
else:
	print(a * 180 / p)