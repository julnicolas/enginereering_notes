#include <iostream>

using namespace std;

// Compile with g++ -std=c++20 -o

// Typed sum metafunction in c++98 style
// introducing dependent types.
template <typename T = int>
struct typed {
	typedef T type;
	
	template <T X, T Y>
	struct sum {
		enum: T {
			value = X+Y,
		};
	};
};

template<typename T, T X, T Y>
consteval T ssum() {
	// typename is mandatory here because sum<T, T>
	// depends on (is a dependant type) of typed<T>.
	// That is, it only exists if typed<T> exists and is
	// instantiated.
	// 
	// Using typename tells the compiler to check types at
	// template instantiation rather than declaration.
	// Check the last statement.
	using t = typename typed<T>::sum<X, Y>;
	// using defines a variable, result of a computation
	// understand a variable as in functional programming style -
	// that is a label on an evaluated expression.
	return t::value;
}

int main(int argc, char* argv[]) {
	cout << ssum<unsigned int, 2, 3>() << endl;
	return 0;
}
