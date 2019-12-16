

A = int(input("A = "))
B = int(input("B = "))
print('A = ', A)
print('B = ', B)

r = A - B
while r >= B:
    r -= B
print("Остаток: ", r)