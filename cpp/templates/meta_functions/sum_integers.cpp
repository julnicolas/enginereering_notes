#include <iostream>
#include <cstdint>

// Returns the sum of two int64s
template <std::int64_t N, std::int64_t M>
struct add {
	enum: std::int64_t { value = N + M };
};

// TODO
// Try to define a recursive sum function with variadic templates

int main(int argc, char* argv[]) {
	static_assert(add<1, 2>::value == 3);

	// commented as intentionally generate a compilation error
	//static_assert(add<4, 2>::value > 6);

	constexpr int v = add<5, 7>::value;
	static_assert(v == 12);
	std::cout << "v == " << v << std::endl;

	static_assert( add<1, add<1, 2>::value>::value == 4  );

	return 0;
}
