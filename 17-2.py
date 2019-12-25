# coding: utf-8
import random
 
 
K = input('K - ')
N = input('N - ')
 
array_n = [[(random.randint(-100, 100)) for i in range(random.randint(1, 10))] for e in range(N)]  
 
if N < K:  
    print(array_n)
else:
    print(array_n)
    print('\n')
 
   
    t_1 = array_n[K-1]
    t_2 = array_n[N-1]
    array_n[K-1] = t_2
    array_n[N-1] = t_1
    print('\n')
 
    
    print(array_n)