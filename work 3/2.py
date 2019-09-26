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