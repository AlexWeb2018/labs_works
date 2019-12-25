# -*- coding: utf-8 -*-
import random

ru_letters = u"абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en_letters = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
tj_letters = u"ғӣқӯҳҷҒӢҚӮҲҶ"
digits = u"0123456789"

letters = ru_letters + en_letters + tj_letters + digits

K = random.randrange(1,21)
S = ''.join(random.choice(letters) for _ in range(K))
C = random.choice(S)

print("K:",K)
print("String:",S)
print("Character: ",C)

S_new = ""
for i in S:
    if i == C:
        S_new += i
    S_new += i
print("New string:",S_new)