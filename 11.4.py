

S_start = 1000
S_end = 1100

P = int(input('P = '))
coef = 1 + P / 100
print("Initial Amount = {0}, Percent = {1}, Coef = {2}".format(S_start,P,coef))
K = 0
S = S_start
while S < S_end:
    S *= coef
    K += 1
    print("K = {0}, S = {1}".format(K,S))

print()
print("Months = {0}, Final Amount = {1}".format(K,S))