a = int(input("Введите значение угла 0 < a < 2p: "))
p = 3.14

if (a <= 0 or a >= 2*p):
	print("Не то число")
else:
	print(a * 180 / p)