# coding: utf-8
import random
 
K = input('K - ')
N = input('N - ')
 
array_n = [[(random.randint(-100, 100)) for i in range(random.randint(1, 10))] for e in range(N)]  # Создать массив
 
if N < K:  # Если N меньше K вывести без изменений
    print(array_n)
else:
    print('%s\n' % array_n)
 
    # Произвести замену
    t_1 = array_n[K - 1]
    array_n[K-1] = array_n[N - 1]
    array_n[N - 1] = t_1
 
    # Вывести измененный массив
    print('%s\n' % array_n)