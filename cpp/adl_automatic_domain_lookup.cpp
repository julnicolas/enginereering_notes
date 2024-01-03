/* ADL - Argument Dependent Lookup
 * This is a compiler feature to automatically find
 * function/methods to call depending on enabled namespaces
 * and provided function arguments.
 *
 * This feature is used at compile time to determine the function/
 * method to call. The compiler then generates related assembly code
 * to call the function/method without indirection.
 */
#include <iostream>
#include <string>

namespace foo {
	void print(const char* str) {
		std::cout << "calling foo::print" << std::endl;
	}

	struct bar {
		public:
			bar(const char* msg): _msg(msg) {}
	
			// Defines a non member function called
			// ::foo::print with 1 parameter of type
			// const ::foo::bar&
			//
			// Why define it as friend? That way it can have 
			// access to bar's internals as a member function would.
			// (though one could rightfully argue it'd be best to use
			// public interfaces).
			//
			// However, as a non-member function, within the right
			// compilation unit, it can be picked up by the compiler
			// while executing the ADL (Argument Dependent Lookup)
			// algorithm.
			//
			// Note - no const version available since it is not a member
			// function! The equivalent implementation would be using
			// public interfaces with const qualifiers.
			friend void print(const bar& b) {
				std::cout
					<< "calling bar::print(const bar&)"
					<< std::endl
					<< "\tmessage: "
					<< b._msg
					<< std::endl;
			}
	
		private:
			std::string _msg;
	};
	// End of foo namespace
}

int main(int argc, char* argv[]) {
	const char* s = "hello world!";
	foo::bar b("hello bar world!");

	// Enable ADL - argument dependent lookup
	// it differs from explicit lookup where the
	// domain resolution operator (::) is used.
	//
	// now :: is the union of :: and ::foo::
	using namespace foo;

	// In :: and ::foo:: only foo::print(const char*)
	// is suitable as a print function.
	print(s);
	// In :: and ::foo:: only foo::print(const bar&)
	// is suitable as a print function.
	print(b);

	return 0;
}
