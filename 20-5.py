# -*- coding: utf-8 -*-
import random
import re

ru_letters = u"абвгдежзийклмнопрстуфхцчшщъыьэюя"
tj_letters = u"ғӣқӯҳҷ"

letters = ru_letters + tj_letters

K = random.randrange(2,21)
S = ''.join(random.choice(letters) for _ in range(K))
print("K:",K)

I_end = random.randint(1,K)
I_start = random.randint(0,I_end)
print("I_start:",I_start)
print("I_end:",I_end)

S0 = S[I_start:I_end]
N = random.randrange(0,3)
print("N:",N)
for i in range(N):
    S += S    
print("String:",S)
print("S0:",S0)

for m in re.finditer(S0, S):
    print('{0} found: {1} - {2}'.format(S0, m.start(), m.end()))