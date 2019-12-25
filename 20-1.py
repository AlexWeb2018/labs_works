import random

N = random.randrange(32, 126)
c = chr(N)
c_prev = chr(ord(c)-1)
c_next = chr(ord(c)+1)

print("Char: ",c)
print("Char prev.: ",c_prev)
print("Char next: ",c_next)