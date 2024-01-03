// std::move must absolutely be called as 'normal' constructors
// create lvalues
// Only values passed in the following cases can be considered
// rvalue or rvalue references:
// - explicitely returned rvalue references
// - literalls
// - std::move lvalue or lvalue references can be considered
// 	rvalue or rvalue references
//
// 	a rvalue is a litteral value or a value that has no existance in memory
// 		-> a static (static as of available at compile time) value
// 	a rvalue reference is either:
// 	- a reference to a rvalue
// 	- a reference to a lvalue but the rvalue references carries a sense of 
// 		change of ownership. Meaning, moved objects shouldn't be reused (as
// 		state is not guaranted). Also, move operators will be called on these
// 		values.
#include <iostream>
using namespace std;

// The following example only shows if passed values are considered
// as lvalue or rvalues (references).
//
// The actual implementation doesn't differ between copy and move operations
// as the data structure is very simple (default operators would normally
// suffice).
struct v {
	v() { cout << " lvalue: constructor; "; }
	v(const v& u): x(u.x) { cout << " lvalue: copy constructor; "; }
	v(v&& u): x(u.x) { mv(" rvalue: move constructor; "); }
	v& operator=(const v& u) { 
		cout << " lvalue: lvalue assignment; ";
		x = u.x;
		return *this;
	}
	v& operator=(v&& u) { 
		mv(" rvalue: move assignment; ");
		x = u.x;
		return *this;
	}
	~v() = default;

	int x = 0;

	private:
		// Prints move related message
		void mv(const char* msg) {
			cout << msg
				<< endl
				<< "\tinput value cannot be reused";
		}
};

std::ostream& operator<<(std::ostream& s, const v& u) {
	return s;
}

int main(int argc, char* argv[]) {
	cout << "creating base object: u of type v;" << endl;
	v u;
	cout << endl << endl;

	cout << "starting test cases:" << endl;
	cout << "v(): " << v() << endl
		<< "v(u): " << v(u) << endl
		<< "v(std::move(u)): "
		<< v(std::move(u))
		<< endl;

	cout << "creating affected object: w of type v;" << endl;
	v w;
	cout << endl << endl;

	cout << "creating target object: z of type v;" << endl;
	v z;
	cout << endl << endl;

	cout << "z = w: ";
	z = w;
	cout << endl;

	cout << "z = std::move(w): ";
	z = std::move(w);
	cout << endl;

	return 0;
}
