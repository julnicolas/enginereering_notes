/* This program explains what happens when an exception is raised from
 * a constructor (copy constructor here but same rule applies for
 * any kind of constructor).
 *
 * It is recommended by isocpp.org to raise exceptions from
 * constructors if construction process cannot be carried out.
 * Though, some guidelines must be respected to avoid leaks
 * (leaks would happen if memory is dynamically allocated from
 * the constructor).
 *
 * If exceptions are not used in your code base, rather use a zombie
 * state approach, meaning constructors return but before, set an
 * internal state to check on object sanity (such as is_healthy).
 *
 * Exception raised from a constructor
 * -----------------------------------
 * - automatic variables are deallocated
 * - constructed fields' destructor are called
 * - exception is passed to the caller's scope
 *
 * Important: constructed object's destructor is *NOT* called.
 * Meaning all objects must carefully manage their resources,
 * no dynamic allocations should be carried out in constructors
 * as corresponding delete operations will not be called.
 * If such allocations, or any other system resource allocations
 * must be done, enclose them into corresponding, fine grained
 * objects.
 *
 */
#include <iostream>
#include <stdexcept>

using namespace std;

// I added this class to check if object members'
// destructors are called when an exception is raised
// from a 'container''s constructor.
// I call a container here an object made up of at least
// one foo object as attribute.
class Foo {
	public:
		~Foo() { 
			cout << "Foo destructor @ == "
			<< this
			<< endl;
		}
};

// Check if A's destructor is called if an exception is raised
// from the copy constructor.
// Answer ~A is not called but constructed fields' destructor
// are (~Foo is called for foo).
class A {
	public:
		A() {
			cout << "called constructor for @ == "
			<< this
			<< endl;
		}
		explicit A(const A&) { 
			cout << "called copy constructor for @ == " 
				<< this
				<< endl
				<< "  @foo == "
				<< &foo
				<< endl;
			throw runtime_error("copy constructor throws");
		}
		~A() { 
			cout << "called destructor for @ == " 
				<< this
				<< endl; 
		}

	private:
		// as foo's the only data struct in this object
		// &foo == this
		Foo foo; 
};

int main(int argc, char* argv[]) {
	A a;
	cout << "&a == " << &a << endl;
	try {
		// ~A is not called for b, though
		// constituting and constructed fields'
		// destructor are (~Foo is called)
		A b(a);
	}
	catch (const runtime_error& e) {
		cout << e.what() << endl;
	}

	cout << "-- end of main" << endl << endl;
	return 0;
}
