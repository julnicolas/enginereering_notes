/* EMPTY BASE OPTIMISATION (EBO)
 *
 * The EBO is an optimisation made by the compiler
 * to not add any extra space to a child class for
 * a stateless ("empty") parent class.
 */
#include <iostream>

// Generally (not specified by the CPP standard), size of an empty
// struct is 1 or can also be expected to be size of a word.
struct TotalyEmpty {};

// Inheritence is public by default with structs
// This struct is said stateless because no dynamic attributes are
// defined.
// There is just a static method which cannot modify any attributes as
// inexistant so it is equivalent to a pure function.
struct StatelessWithStatic: TotalyEmpty {
	static int foo() {
		return 2;
	}
};

// If EBO is implemented then sizeof(Stateful) is 3*sizeof(int)
// Indeed, TotalyEmpty does not define anything so does not bring any
// additional context or features to Stateful.
// Then, Stateless... only defines a pure function.
// Therefore, no extra space is needed for stateful to function.
// This is the reasoning EBO relies on.
struct Stateful: StatelessWithStatic {
	int x;
	int y;
	int z;
};

int main(int argc, char* argv[]) {
	// if compiled with EBO sizeof(Stateful) == 3 * sizeof(int)
	static_assert(sizeof(Stateful) == 3*sizeof(int), "program has not been compiled with EBO optimisation");

	std::cout << "sizeof(Stateful) == " << sizeof(Stateful) << std::endl;
	std::cout << "sizeof(int) == " << sizeof(int) << std::endl;

	return 0;
}
