N = input('N = ')
#a = [2*(i+1) for i in range(N)]
A = input('A = ').split()[:N]
B = []
C = []
print("N = ", N)
print("Array A:")
print(A)

x = A[0]
B.append(x)
C.append(1)
k = 0
for i in range(1,N):
    if x == A[i] :
        C[k] += 1
    else :
        x = A[i]
        B.append(x)
        C.append(1)
        k += 1       
print()
print("Array B:")
print(B)
print("Array C:")
print(C)