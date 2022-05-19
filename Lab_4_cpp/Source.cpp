#include <iostream>
#include "Header.h"

using namespace std;

int main() {
	Ring C1;
	Ring C2(1, 2, 3, 4);
	Ring C3(C2);
	cout << "Before:\n";
	cout << "\nC1\n"; output(C1);
	cout << "\nC2\n"; output(C2);
	cout << "\nC3\n"; output(C3);
	++C1;
	C2++;
	C3 *= 2;
	cout << "\nAfter:\n";
	cout << "\nC1\n"; output(C1);
	cout << "\nC2\n"; output(C2);
	cout << "\nC3\n"; output(C3);
	cout << endl;
	float Thickness = Find(C1.thickness(), C2.thickness(), C3.thickness());
	cout << "\nIts thickness is " << Thickness << endl;
}