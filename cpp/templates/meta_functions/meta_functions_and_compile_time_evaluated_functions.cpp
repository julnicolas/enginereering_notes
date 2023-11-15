#include <iostream>

// Compile with g++ -std=c++20 -o

using namespace std;

// C++98 style - make a typed struct with several embedded operations
// Only sum is defined
// open to extension can accept a different amount of parameters
// Though introduces a more complex type and dependent types (that must
// be used with typename)
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

// C++98 style - a simpler implementation using a single metafunction with
// no wrapping struct to type the metafunction.
template<typename T, T X, T Y>
struct add98 {
	enum : T {
		sum = X + Y,
	};
};

// C++11 style -  uses the constexpr keyword
// It means it can also be executed if the evealution does not
// correspond to compile time constants.
//
// Notice - this is a c++ function not a metafunction
template<typename T, T X, T Y>
constexpr T add11() {
	return X + Y;
}

// C++20 style - this is an immediate function.
// It can only returns compile-time-computed constants.
//
// Note - this is a c++ function not a metafunction
template<typename T, T X, T Y>
consteval T add20() {
	return X + Y;
}


int main(int argc, char* argv[]) {
	cout << typed<>::sum<2, 3>::value << endl;
	cout << add98<unsigned int, 4, 5>::sum << endl;
	cout << add11<unsigned int, 5, 6>() << endl;
	cout << add20<unsigned int, 7, 8>() << endl;
	return 0;
}
