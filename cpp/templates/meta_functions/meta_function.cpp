#include <iostream>

// A metafunction is a function in the mathematical sense
// which maps entry values to output values at compile time.
//
// They allow to compute values at compilation time by the compiler.
// They differ from instant and constexpr functions in the sense that
// they are not c++ functions, they are compiler only functions.
// Though, the same computings can be done with either constructs.
//
// A way to do so is use structs and enums as follows.

using namespace std;

template<typename int_t, int_t X, int_t Y>
struct sum {
	enum : int_t {
		value = X + Y,
	};
};

int main(int argc, char* argv[]) {
	cout << sum<unsigned int, 2, 3>::value << endl;
	return 0;
}
