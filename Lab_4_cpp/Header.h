#pragma once

class Ring {
	float cordX, cordY,
		innerRadius, outerRadius;
	public:
		Ring();

		Ring(float CordX, float CordY, float InnerRadius, float OuterRadius);

		Ring(Ring& ring);

		~Ring(){}

		float thickness();

		Ring operator++();

		Ring operator++(int useless);

		const Ring operator*=(int size);

		float getcordX();

		float getcordY();

		float getInnerRadius();

		float getOuterRadius();

};
float Find(float C1, float C2, float C3);
void output(Ring);
