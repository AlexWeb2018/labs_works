x = int(input('x = '))
y = int(input('y = '))

if (x > 0 and y > 0):
	print('1 chetvert')
elif (x < 0 and y > 0):
	print('2 chetvert')
elif (x < 0 and y < 0):
	print('3 chetvert')
else:
	print('4 chetvert')