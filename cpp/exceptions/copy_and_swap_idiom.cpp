/* Copy-and-swap idiom
 *
 * This is an idiom, series of step, to code
 * a class' assignment operator using the
 * copy operator while guaranteeing strong
 * exception safety.
 *
 * How to implement it? [operator=(const T& t)]
 * --------------------------------------------
 * - construct a copy of t as temporary object
 *   using the copy constructor
 *   - copy must guarantee strong exception safety
 *   	itself (to avoid resource leaks). As proved 
 *   	below, if copy constructors verify basic
 *   	exception safety then per design they also
 *   	guarantee strong exception safety.
 * - if copying throws then 'this' is not afected
 *   then guarantying a predictable object state
 * - then once the copy is done, swap the copy with
 *   this.
 * - return *this
 *
 * How to implement swap?
 * ----------------------
 * - swap must be no-throw, otherwise strong exception
 *   safety cannot be guaranteed
 * - swap for T must swap every fields of 'this' with temp
 *   calling swap (thus keeping on guaranteeing the no-throw
 *   property)
 * - swap must be declared as a public friend function so that
 *   it can have access to objects' internals as a method would
 *   (and it should have been a method) and, it is available to
 *   the compiler while executing its ADL 
 *   (Argument Dependent Lookup) algorithm.
 *
 * Proof that strong exception safety is guaranteed
 * ------------------------------------------------
 * - Here are, in order, all executed statements:
 *   - Copy constructor on temporary resulting in temporary
 *   	value. Copy is strong exception safe.
 *   - Copy being strong exception safe they are no risk of leaking
 *   resources while making the temporary value. Therefore strong
 *   exception safety is maintained.
 *   - if an exception is raised while creating the copy, the main
 *   object's state hasn't been modified and as said before no resources
 *   have been leaked. Therefore exception safety is maintained.
 *   - swap is no-throw guaranted so state is predictible and no resources
 *   are leaked. Therefore strong exception is still maintained.
 *   - Then, a reference on *this is returned which is by definition
 *   a no-throw operation. Therefore strong exception safety is maintained.
 *
 * - Finally as strong-exception safety is maintained for every steps
 *   of the function, then by transitivity the function is strong exception
 *   safe.
 *
 * Proof - if copy constructor is basic/weak exception safe then it is
 * ------------------------------------------------------------------
 * strong exception safe
 * ----------------------
 * If the copy constructor is basic exception safe then by definiton it
 * guarantees that:
 * - no resources are leaked
 * - object is destructible or usable but state is not determined
 *
 * Strong exception safety adds the property that an object's state is
 * not modified if an exception is raised.
 *
 *	Now let us look at the state of a constructed object:
 *	- before construction it has no location in memory.
 *	- when an exception occurs, no resources are leaked as per
 *	the weak exception safety property and objects' struct is cleaned
 *	up for memory. Therefore the object is not present in memory.
 *	- This is the same state as before creation, therefore state has
 *	not changed. Therefore the additional strong safety rule is verified.
 *
 *	In conclusion as the constructor is already weak exception safe and
 *	that it verifies the no-state-change property, it is strong exception
 *	safe.
 *
 * - 
 */

//#include <algorithm> // std::swap's location until c++ 11
#include <utility> // std::swap's location since c++ 11
#include <iostream>
#include <vector>

template <typename T>
class Foo {
	public:
		Foo() = default;
		explicit Foo(const T& t): _data(t) {}

		Foo(const Foo&);
		Foo& operator=(const Foo&);

		// overload std::swap to enable ADL-based swap
		// swap is a non-member function defined in ::
		//
		// However, as being defined in ::Foo it has access to
		// ::Foo as if it were a member function.
		// This is OK to do so as we'd like swap to be an internal function
		// but to be accessible via ADL so that proper swap function can
		// be used depending on arguments' type.
		//
		// Why using template<typename U>?
		// Because swap is not a Foo member function therefore it must
		// be generated when used.
		//
		// Note - writting the function body may temper with the 
		// function generation as it is itself in a templated class.
		template <typename U>
		friend void swap(Foo<U>& base, Foo<U>& copy);

		// Print function
		// Non-member function with internal access to object.
		// Breaks the encapsulation principle. Though... mostly
		// because of how the c++ interface to render an object is designed.
		// 
		// Creating a __to_str__ method in python is not really useful as
		// the overloaded function << would need to call it.
		template <typename U>
		friend std::ostream& operator<<(std::ostream& stream, const Foo<U>&);

	private:
		T _data;
};

// Strong exception safe
template <typename T>
Foo<T>::Foo(const Foo& o) {
	std::cout << "foo's copy constructor" << std::endl;
	
	// std containers copy constructors are strong exception
	// safe
	_data = o._data;
}

// Strong exception safe
template <typename T>
Foo<T>& Foo<T>::operator=(const Foo& o) {
	// Strong exception safe
	Foo<T> tmp = o;

	// no-throw
	swap(*this, tmp);

	// no-throw
	return *this;
}

// no-throw
template <typename T>
void swap(Foo<T>& base, Foo<T>& copy) {
	// Enable ADL - Argument Dependent Lookup
	// That is, let the compiler deduce best swap function
	// to call based on arguments' type.
	// Concretely, either from std or one of our own.
	using namespace std;

	cout << "swap for Foo" << endl;

	// Swap attribute per attribute
	// This is possible as swap is expected to be nothrow
	swap(base._data, copy._data);
}

template <typename T>
std::ostream& operator<<(std::ostream& stream, const Foo<T>& foo) {
	stream << "{ data: " << foo._data << "}";

	return stream;
}


int main(int argc, char* argv[]) {
	Foo<int> fooi(1);
	Foo<int> fooi2(2);
	std::cout << "before assignment:" << std::endl
		<< "\tfooi == " << fooi << std::endl
		<< "\tfooi2 == " << fooi2 << std::endl << std::endl;

	fooi2 = fooi;

	std::cout << std::endl << "after assignment:" << std::endl
		<< "\tfooi == " << fooi << std::endl
		<< "\tfooi2 == " << fooi2 << std::endl;

	return 0;
}
