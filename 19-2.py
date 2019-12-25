M = [[4, 7, 2, 9],
     [2, 5, 8, 4],
     [8, 1, 7, 3]]
for i in M:
    print(i)
print('\nматрица после преобразования:\n')
M1 = []
m = len(M)
n = len(M[0])
minXY = [0,0]          # координаты минимального элемента
maxXY = [0,0]          # координаты максимального элемента
p = M[0][0]            # значение текущего элемента
for i in range(m):
    for j in range(n):
        if M[i][j] < p:
            minXY = [i,j]
            p = M[i][j]
p = M[0][0]
for i in range(m):
    for j in range(n):
        if M[i][j] > p:
            maxXY = [i,j]
            p = M[i][j]
def repl(L, c1, c2):
    p1 = L[c1]
    p2 = L[c2]
    L.pop(c1)
    if c1 == m:
        L.append(p2)
    else:
        L.insert(c1, p2)
    L.pop(c2)
    if c2 == m:
        L.append(p1)
    else:
        L.insert(c2, p1)
    print(L)
    M1.append(L)
 
for i in range(m):
    repl(M[i], minXY[1], maxXY[1])
print('\n', M1)