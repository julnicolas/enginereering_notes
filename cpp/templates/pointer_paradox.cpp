#include <iostream>

/*
	Please do read along pointer_paradox_companion.cpp.

	The two last calls seem surprising but the compiler instantiates
	function types based on type deduction.

	That is, let us define p as double p;

	In that case type of &p is double*.

Given:
	template<typename T>
	void f(const T*);
and:
	template<typename T>
	void f(const T&);

	Then let us substitute T by double* in both above expressions to obtain:
	T = double*
	void f(const double**);

	T = double*
	void f(cont double*&);

	Finally let us define the following variable:
	double p = 5.2;
	f(&p); // &p is of type double* the same as the fixed T type from above.
	
	Then as showed in the previous step, two functions are automatically
	generated by the compiler:
		void f(const double**);
		void f(const double*&);

	However by c++'s language grammar:
		- double* can unexplicitely convert to const double* &
			(a const reference variable is created to hold the pointer value)
		- double* is a different type from double** and cannot be converted
			by default nor unexplicitely from double* to double**.

	Hence, the function being called when stating f(&p) is
		void f(const double*&);
*/

using namespace std;

template<typename T>
void f(const T* v) {
	cout << "I'm a pointer" << endl;
}

template<typename T>
void f(const T& v) {
	cout << "I'm a reference" << endl;
	cout << "Here's my value: " << v << endl;
}

int main(int argc, char* argv[]) {
	const char* s = "hello world";

	// Calls the const T* version
	f(s);
	// Calls the const T& version
	f(3.14);

	double p = 53.2;
	// Calls the const T& version
	// Displayed value is a pointer which validates the above
	// explanation.
	f(&p);

	const double q = 53.2;
	// Calls the const T& version
	// Displayed value is a pointer which validates the above
	// explanation.
	f(&p);

	return 0;
}
