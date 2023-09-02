#include <iostream>

/* This example shows that const/non const declarations are considered distincts
 * by c++. Make sure to define both methods if ambiguity can exist.
 *
 * The const version of a function is called if a const reference is passed, the non
 * const if the reference is not const.
 *
 * If only of the two forms are defined, the const version can be called in a non
 * const function. However if a const function tries to call said method but only
 * a non const version is implemented, then it results in a compilation error.
 *
 * Finally, if a parent class defines a const version of a method as virtual but a child
 * class defines a non const version with the same signature (except the const property).
 * If, a function const references the child object then the parent's const version will
 * be called and the non-const apparently overriding version will not be.
 *
 * Note: To have the compiler output an error if one attempts to override a function version
 * (const or not) use the override specifier. An error will only be thrown by the compiler if
 * only one of the two versions is defined and the wrong one is beeing overriden.
*/

using namespace std;

class Base {
	public:
		virtual void f() const;
		virtual void f();
		virtual ~Base() = default;
};

void Base::f() const {
	cout << "base const" << endl;
}

void Base::f() {
	cout << "base non const, calling const..." << endl;
	const Base& t = *this;
	t.f();
}

class Child: public Base {
	public:
		virtual void f() const;
		virtual void f();
		virtual ~Child() = default;
};

void Child::f() const {
	cout << "child const" << endl;
}	

void Child::f() {
	cout << "child not const" << endl;
}	

void print(Base& b) {
	cout << "from print:" << endl;
	b.f();
	cout << "===" << endl;
}

void print_const(const Base& b) {
	cout << "from print_const:" << endl;
	b.f();
	cout << "===" << endl;
}

int main(int argc, char* argv[]) {
	Base b;
	Child c;

	print(b);
	print(c);
	print_const(b);
	print_const(c);

	return 0;
}
