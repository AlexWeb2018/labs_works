

N = int(input("N = "))

K = 1
S = 1
while S < N:
    K += 1
    S += K
    print("K = {0}, S = {1}".format(K,S))

print()
print("K = {0}, S = {1}".format(K,S))