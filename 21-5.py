file = open('input.txt','r')
list_str = file.read().split('\n')
file.close()
 
max_len = len(sorted(list_str,key = len,reverse = True)[0])
print('максимальная длина строки =',max_len)
print('строки содержащие более двух слов:')
print(*(i for i in list_str if len(i.split())>2),sep = '\n')
