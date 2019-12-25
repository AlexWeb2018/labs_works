# Дано вещественное число — цена 1 кг конфет. 
# Вывести стоимость 0.1, 0.2, . . . , 1 кг конфет

	
price = int(input('prise - '))
print('Цена 1 кг конфет: ', price)
print()
for i in range(1,11):
    x = 0.1 * i
    print('Стоимость {0:.1f} кг: {1:.2f}'.format(x, x * price))
print()