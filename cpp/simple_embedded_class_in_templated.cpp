#include <iostream>
#include <string>

using namespace std;

template <typename T>
class A {
	public:
		class B {
			public:
				explicit B(const T& t);
				A<T> add(const T& t);
			private:
				T _t;
		};

		explicit A(T t);
		void print() const;

		A<T> operator+(T t1) const;
	private:
		T _t;
};

template <typename T>
A<T>::A(T t): _t(t) {}

template <typename T>
void A<T>::print() const {
	cout << _t << endl;
}

template<typename T>
A<T> A<T>::operator+(T t1) const {
	return std::move(A<T>(_t + t1));
}

template<typename T>
A<T>::B::B(const T& t): _t(t) {}

template<typename T>
A<T> A<T>::B::add(const T& t) {
	return std::move(A<T>(_t + t));
}

int main(int argc, char* argv[]) {
	A<int> ai(2);
	A<string> as("hello");

	ai.print();
	as.print();

	(ai + 4).print();
	(as + " world").print();

	A<int>::B b(3);
	A<int> a = std::move(b.add(2));
	a.print();

	return 0;
}
