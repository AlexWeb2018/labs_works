#  Даны переменные A, B, C. Изменить их значения, переместив
# содержимое A в B, B — в C, C — в A, и вывести новые значения переменных
# A, B, C.


a = int(input());
b = int(input());
c = int(input());

bufa = a;
bufc = c;


a = bufc;
c = b;
b = bufa;

print(a);
print(b);
print(c);