a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))


ab = abc(b - a)
ac = abc(c - a)

if (ab < ac):
	print("точка b ближе, ab = ", ab)
else if (ac < ab):
	print("точка c ближе, ac = ", ac)
else if(ab = ac):
	print("точки b и c равноудалены от a")