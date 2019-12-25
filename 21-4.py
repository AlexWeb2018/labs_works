pattern = ['й', 'у', 'е', 'ё', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
 
with open('text.txt', encoding='utf-8') as f:
   str = [i.lower() for i in list(f.read()) if i != ' ']
 
tmp = [ch for ch in str if ch in pattern]
 
print('Гласных: {} \nСогласных: {}'.format(len(tmp), len(str)-len(tmp)))
