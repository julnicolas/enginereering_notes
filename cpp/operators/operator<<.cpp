/* operator<< is the operator to 
 * append to an output stream.
 *
 * The output stream by default is stdout.
 *
 */
#include <iostream>
#include <sstream>
#include <string>

namespace from_foo {
	template <typename T>
	class foo {
		public:
			explicit foo(const T& t): _data(t) {}
			std::string to_str() const { 
				return (std::stringstream("") << _data).str();
			}
		
		private:
			T _data;
	};

	// Define the operator as a non-member function
	// it needs sufficient public interfaces to be able to render objects
	//
	// Gotcha - Do not forget the reference as basic_stream do not have copy constructors
	template <typename T>
	std::ostream& operator<<(std::ostream& stream, const foo<T>& f) {
		stream << f.to_str();
		return stream;
	}
}

template <typename T>
class bar {
	public:
		explicit bar(const T& t): _data(t) {}

		// define the function as a non-member function but with priviledged
		// access to private and protected parts.
		//
		// this breaks the encapsulation principle, though use a friend function
		// is constrained by the ostream interfaces from the std lib.
		//
		// an additional templated type must be defined because operator<< is a non-
		// member function, that is exterior to the bar class. That means a new 
		// operator<< <T> function must be defined for every bar<T> classes.
		//
		// Note - if writting this friend functions an inline body in the class, the function
		// might not be regenareted for a different type.
		// Hence the actual definition outside of the class body to enforce code generation.
		template <typename U>
		friend std::ostream& operator<<(std::ostream& s, const bar<U>& b);

	private:
		T _data;
};

template <typename U>
std::ostream& operator<<(std::ostream& s, const bar<U>& b) {
	return s << b._data;
}

namespace str_functions {
	std::string s(const char* msg) {
		return std::string(msg);
	}
}

// construct std::string from move constructor
// std::move must absolutely be called as std::string()
// creates a lvalue
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
#define s(cstr) std::move(str_functions::s(cstr))

int main(int argc, char* argv[]) {
	using namespace std;
	
	cout << "using non-member (without friend) operator<<:" << endl
		<< from_foo::foo(s("hello world!")) << endl << endl
		<< from_foo::foo(123) << endl << endl
		<< "using non-member function (with friend qualifier) operator<<"
		<< endl
		<< bar(s("salut tout le monde!")) << endl << endl
		<< bar(456) << endl << endl;
		
	return 0;
}
