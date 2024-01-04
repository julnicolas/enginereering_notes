/* noexcept specifier
 * Tells the compiler labelled function cannot throw
 * exceptions. If an exception is effectively thrown while
 * executing, std::terminate will be called.
 *
 * The specifier remplaces the old and deprecated throw()
 *
 * Noexcept does not make a function overloadable. Meaning
 * that a noexcept and noexcept-free version of the same
 * function cannot coexist (same logic as different return
 * types are not sufficient for overloading).
 *
 * This code compiles with a warning. This is normal, as 
 * a method throws despite being noexecpt-declared. This
 * is to show std::terminate is called in this context.
 */

#include <stdexcept>
#include <iostream>

template <typename T>
class Foo {
	public:
		using ptr_t = char*;
		// Evaluates to either true or false
		// therefore it is possible to specialise templates using
		// 	noexcept(true) or noexcept(false)
		// 	instead of noexcept(sizeof(T) <= sizeof(ptr_t))
		//
		// 	Generic and recommended way:
		// 	noexcept(except_cond)
		enum: bool { except_cond = sizeof(T) <= sizeof(ptr_t),};

		Foo() = default;
		explicit Foo(const T& t): _data(t) {}

		// use noexcept(expression) to determine if exceptions should
		// be thrown or std::terminate should be called instead.
		//
		// noexcept(expression) evaluates to
		// 		noexcept(true) or noexcept(false)
		// 		noexcept(true) is equivalent to noexcept
		// 		(without a parenthesized expression)
		// If noexcept(expression) <=> noexcept(true)
		// then no exceptions will be raised and std::terminate
		// will be called instead.
		void raise() noexcept(except_cond);

	private:
		T _data;

		void raise_noexcept() noexcept;
		void raise_except() noexcept(false);
};

template <typename T>
void Foo<T>::raise() noexcept(except_cond) {
	// noexcept operator
	// compile time check whether Foo<T>::raise is
	// defined noexcept or not.
	// Then execute the noexcept or except version.
	// With modern branch prediction this if/else
	// block has no impact on performace (maybe on
	// just first execution for every type).
	//
	// after check is equivalent to if(true)/else
	// or if (false)/else
	if (noexcept(raise())) {
		raise_noexcept();
	} else {
		raise_except();
	}
}

template <typename T>
void Foo<T>::raise_noexcept() noexcept {
	std::cout << "not raising" << std::endl;
}

template <typename T>
void Foo<T>::raise_except() noexcept(false) {
	throw std::runtime_error("raising!");
}

// Specialise noexcept template to raise an exception
// to show that in this case std::terminate is called
// in place of passing the exception up.
using raise_from_no_except_t = struct {};

template <>
void Foo<raise_from_no_except_t>::raise() noexcept(true) {
	// Make sure noexcept is true
	static_assert(Foo<raise_from_no_except_t>::except_cond);

	std::cout << "Foo<raise_from_no_except_t>::raise" << std::endl;

	// terminate will be called after throwing this exception
	throw std::runtime_error("throwing from noexcept function");
}

int main(int argc, char* argv[]) {
	try {
		// Will not raise
		Foo(2).raise();

		// Raise but is noexcept(false)
		using raise_t = struct {int _fill[3];};
		Foo<raise_t>(raise_t{}).raise();
	}
	catch (std::runtime_error& e) {
		std::cerr << e.what() << std::endl;
	}

	// Try catch block but exception will not be caught
	// as function raise is noexcept for this struct.
	// terminate will be called then.
	try {
		Foo<raise_from_no_except_t>(raise_from_no_except_t{}).raise();
	}
	catch (std::runtime_error& e) {
		std::cerr << e.what() << std::endl;
	}
	std::cout << "end of main" << std::endl;

	return 0;
}
