#include <iostream>
using namespace std;

template <typename int_t, int_t I>
struct strong_type {
	enum : int_t { value = I };
};

template <typename T, typename U>
constexpr bool eq() {
	// do an apparently useless static cast so that operations can be optimized out
	// by the compiler.
	//
	// Both casting direction are tested so that covarient types can be evicted (which happens
	// between parent and child classes).
	static_cast<T>(U());
	static_cast<U>(T());
	return true;
}

template <int N, int M>
struct add {
		enum { r = N + M  };
};

template <typename int_t, int_t N, int_t M>
struct sadd {
	using type = strong_type<int_t, N + M>;
};


template <typename int_t, int_t N, int_t M>
constexpr strong_type<int_t, N + M> strong_add(strong_type<int_t, N>, strong_type<int_t, M>) { return strong_type<int_t, N + M>{}; }

template <typename int_t, int_t N, int_t M>
struct strong_add2 {
	using type = strong_type<int_t, N + M>;
	static constexpr strong_add2<int_t, N, M> add(strong_type<int_t, N>, strong_type<int_t, M>) { return strong_add2<int_t, N, M>{}; }
};

int main(int argc, char* argv[]) {
	static_assert(add<1, 2>::r == 3, "bad sum");

	// Try to implment the same using strong ints!
	auto r = add<3, 4>::r;
	cout << r << endl;

	// This is how to define a variable in meta template programing.
	using two_i64 = strong_type<long long int, 2>;
	using four_i64 = strong_type<long long int, 4>;
	using two_ui64 = strong_type<unsigned long long int, 2>;

	static_assert(eq<two_i64, two_i64>(), "not equal strong types");
	static_assert(eq<strong_type<int, 2>, strong_type<int, 2>>(), "not equal strong types");
	//static_assert(eq<two_i64, two_ui64>(), "not equal strong types");
	//static_assert(eq<strong_type<unsigned int, 2>, strong_type<int, 2>>(), "not equal strong types");
	//static_assert(eq<strong_type<int, 3>, strong_type<int, 2>>(), "not equal strong types");
	
	using four = sadd<long long int, 2, 2>::type;
	using five = sadd<long long int, 3, 2>::type;
	//using four = strong_add(two_i64(), two_i64());
	static_assert(eq<four, four_i64>() , "invalid sum");
	//static_assert(eq<five, four_i64>() , "invalid sum");
	//static_assert(strong_add<long long int, 2, 2>(two_i64(), two_i64())::value == 4 , "invalid sum");
	static_assert(eq<strong_add2<long long int, 2, 2>::add(two_i64(), two_i64())::type, four>() , "invalid sum");
	
	return 0;
}
