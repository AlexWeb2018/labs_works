a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if (a < b):
	min = a
else:
	min = b

if (c < min):
	min = c

s = a + b + c - min
print(s)