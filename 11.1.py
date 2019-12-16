

A = int(input("A = "))
B = int(input("B = "))

print("A = ", A)
print("B = ", B)
print()

for i in range(A,B + 1):
    for j in range(0, i):
        print(i, end=" ")
    print()