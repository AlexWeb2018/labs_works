# -*- coding: utf-8 -*-
import random
import string

ru_letters = u"абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ"
en_letters = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
tj_letters = u"ғӣқӯҳҷҒӢҚӮҲҶ"

en_Upper = u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = random.randrange(1,10)
s_ru = random.sample(ru_letters, N)
print("RU:",s_ru)

N = random.randrange(1,10)
s_en = random.sample(en_letters, N)
print("EN:",s_en)

N = random.randrange(1,10)
s_tj = random.sample(tj_letters, N)
print("TJ:",s_tj)

N = random.randrange(1,10)
s_digit = random.sample(string.digits, N)
print("Digits:",s_digit)

s = s_ru + s_en + s_tj + s_digit + [' ',' ']
random.shuffle(s)
s = "".join(s)
print(s)

k = 0
for c in s:
    if c in en_Upper:
        k += 1
print("Number of Upper Latin letters:",k)