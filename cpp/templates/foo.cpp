#include <iostream>

/*
 Please do check pointer_paradox.cpp.

 No paradox here as function signatures are not automatically
 deduced by the compiler. There are exact matches between
 declared types and defined functions. Which is not the case
 with the template version! Check it out!

 */

using namespace std;


void f(const double* v) {
	cout << "I'm a pointer" << endl;
}

void f(const double& v) {
	cout << "I'm a reference" << endl;
}

int main(int argc, char* argv[]) {
	// Calls the const double& version
	f(3.14);

	double p = 53.2;
	// Calls the const double* version
	f(&p);

	const double q = 53.2;
	// Calls the const double* version
	f(&p);

	return 0;
}

