

A = int(input("A = "))
B = int(input("B = "))
print("A = {0}, B = {1}".format(A,B))
while B > 0:
    A,B = B,A % B
print("НОД: ",A)