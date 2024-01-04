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
 * Meaning all objects must carefully manage their resources.
 *
 * What about dynamically allocated memory from constructors?
 * ----------------------------------------------------------
 * Let us remind that operator new returns a pointer to the 
 * allocated object. Therefore, the corresponding attribute
 * storing the address is a pointer.
 *
 * Now there is a big difference between raw pointers and smart
 * pointers.
 *
 * Let's say the allocation goes well, the return value is stored
 * in a raw pointer. After that, an exception is raised within the
 * executing constructor. Therefore, as per above, all constructed
 * fields' destructor is called. However, a raw pointer is merelly
 * an int value. That means it doesn't have any destructor attached
 * to it. Therefore its destructor is not executed.
 *
 * Then, as the failing constructor's corresponding destructor is not
 * executed (as the object is partially constructed), previously allocated
 * memory is not freed, thus resulting in a memory leak.
 *
 * Now, let us say that instead of storing operator new's result in a raw pointer
 * it is stored in a smart pointer. Then corresponding smart pointer's destructor
 * will be executed thus freeing the memory. Therefore, the memory leak is
 * prevented.
 *
 * What about operator new?
 * ------------------------
 * As per the C++ standard if during a call to new, an exception is
 * raised from a constructor, a matching (operator new) deallocation
 * function is called to free memory. Then the exception is passed
 * further up. If such deallocation cannot be found, then the exception
 * is passed but memory is not freed. It results in a memory leak.
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
