#include <iostream>
#include "Header.h"

using namespace std;
//Конструктор без параметрів
Ring::Ring() {
	cordX = 3;
	cordY = -3;
	innerRadius = 5;
	outerRadius = 10;
}
//Конструктор з параметрами
Ring::Ring(float CordX, float CordY, float InnerRadius, float OuterRadius) {
	cordX = CordX;
	cordY = CordY;
	innerRadius = InnerRadius;
	outerRadius = OuterRadius;
}
//Конструктор копіювання
Ring::Ring(Ring& ring) {
	cordX = ring.cordX;
	cordY = ring.cordY;
	innerRadius = ring.innerRadius;
	outerRadius = ring.outerRadius;
}
//Товщина кільця
float Ring::thickness() {
	return outerRadius - innerRadius;
}
//Перевантаження оператора префіксного інкрементування
Ring Ring::operator++() {
	++innerRadius;
	return *this;
}
//Перевантаження оператора постфіксного інкрементування
Ring Ring::operator++(int useless) {
	outerRadius++;
	return *this;
}
//Перевантаження оператора множення
const Ring Ring::operator*=(int size) {
	outerRadius *= size;
	return *this;
}
float Ring::getcordX() {
	return cordX;
}
float Ring::getcordY() {
	return cordY;
}
float Ring::getInnerRadius() {
	return innerRadius;
}
float Ring::getOuterRadius() {
	return outerRadius;
}
//Пошук найтовщого кільця
float Find(float C1, float C2, float C3) {
	float amount[]{C1,C2,C3};
	int index = 0;
	float TheThickest = 0;
	for (int i = 0; i < 3; i++) {
		if (amount[i] > TheThickest) {
			TheThickest = amount[i];
			index = i + 1;
		}
	}
		cout << "The thickest ring is C" << index;
	return TheThickest;
}
void output(Ring C) {
	cout << "Cord X: " << C.getcordX() << endl << "Cord Y: " << C.getcordY() << endl <<
		"Inner Radius: " << C.getInnerRadius() << endl << "Outer Radius: " << C.getOuterRadius() << endl;
}
