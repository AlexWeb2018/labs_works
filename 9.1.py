# Дан номер дня – целое число от 1 до 31 и месяца — целое число в диапазоне 
# 1–12 (1 — январь, 2 — февраль и т. д.). 
# Вывести дату в виде текста (например, «пятое января»).


a = int(input('day = '))
b = int(input('month = '))
s = ''
if (a > 9 and a < 20):
	if (a == 10):
		s = 'Десятое';
	elif (a == 11):
		s = 'Одиннадцатое';
	elif (a == 12):
		s = 'Двенадцатое';
	elif (a == 13):
		s = 'Тринадцатое';
	elif (a == 14):
		s = 'Четырнадцатое';
	elif (a == 15):
		s = 'Пятнадцатое';
	elif (a == 16):
		s = 'Шеснадцатое';
	elif (a == 17):
		s = 'Семнадцатое';
	elif (a == 18):
		s = 'Восемнадцатое';
	elif (a == 19):
		s = 'Девятнадцатое';




	elif (a > 19 and a < 30):
			s = 'Двадцать';
	elif (a > 29):
			s = 'Тридцат';
	elif (a > 19 and a < 20):
		if (a == 20 or a == 30):
			s = s + "ое";
	elif (a > 19):
		s = s + "ь ";
	elif (a % 10 == 1):
		s = s + 'первое ';
	elif (a % 10 == 2):
		s = s + 'второе';
	elif (a % 10 == 3):
		s = s + 'третье ';
	elif (a % 10 == 4):
		s = s + 'четвертое ';
	elif (a % 10 == 5):
		s = s + 'пятое ';
	elif (a % 10 == 6):
		s = s + 'шестое ';
	elif (a % 10 == 7):
		s = s + 'седьмое ';
	elif (a % 10 == 8):
		s = s + 'восьмое ';
	elif (a % 10 == 9):
		s = s + 'девятое ';
if (b == 1):
	s = s + 'января';
elif (b == 2):
	s = s + 'февваря';
elif (b == 3):
	s = s + 'марта';
elif (b == 4):
	s = s + 'апреля';
elif (b == 5):
	s = s + 'мая';
elif (b == 6):
	s = s + 'июня';
elif (b == 7):
	s = s + 'июля';
elif (b == 8):
	s = s + 'августа';
elif (b == 9):
	s = s + 'сентября';
elif (b == 10):
	s = s + 'октября';
elif (b == 11):
	s = s + 'ноября';
elif (b == 12):
	s = s + 'декабря';

print(s)