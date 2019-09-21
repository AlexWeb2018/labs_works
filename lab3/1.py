# Поменять местами содержимое переменных A и B и вывести новые
# значения A и B.


a = int(input());
b = int(input());

buf = a;
a = b;
b = buf;

print(a);
print(b);