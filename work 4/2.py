pi = 3.14
a = int(input("Введите градусную меру 0 <= A < 360: "))

if(0 <= a and 360 > a):
	rad = pi * a / 180
	print(rad)
else:
	print("Ниправильнаааа")