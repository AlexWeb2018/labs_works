def Sign(X):
    if X < 0:
        return -1
    elif X > 0:
        return 1
    return 0

A = int(input("A = "))
B = int(input("B = "))



s_A = Sign(A)
s_B = Sign(B)
print("Sign(A) = ", s_A)
print("Sign(B) = ", s_B)
print("Sign(A) + Sign(B) = ", s_A+s_B)