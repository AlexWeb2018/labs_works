#include <iostream>;
#include 
using namespace std;

void main 
{
	int a, b;
	double pi = 3.14;
	cout << "Введите значение угла в радианах";
	cin >> a;
	if (a >= 0) and (a < 2*pi) {
		b = (pi*a)/180;
		cout << "Значение угла в градусах: " << b;
	}
	else {
		cout << "число должно соответствовать условию";
	}
}