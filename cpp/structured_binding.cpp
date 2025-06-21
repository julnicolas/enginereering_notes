#include <iostream>
#include <utility> // std::pair

/* Structured Binding
 *
 * This is a new syntax (C++ 17) to bind enumerable collections
 * to a set of variables. Available classes are pair, tupple.
 *
 * Maybe some other can be added to the list
*/

using namespace std;

pair<int, bool> some_pair(int x, bool p) {
	return std::pair(x+1, p);
}

int main(int argc, char* argv[]) {
	auto [x, p] = pair{1, true};
	cout << "x == " << x << " p == " << p << endl;

	// To reuse the same x, p without reusing auto
	// one needs to use std::tie
	// Otherwise x and p would be shadowed in the scope below
	// And actually this is forbidden by the compiler!
	{
		std::tie(x, p) = some_pair(x, p);
		cout << endl << "Reusing x and p:" << endl;
		cout << "x == " << x << " p == " << p << endl;
	}

	cout << endl << "checking values are the same out of scope" << endl;
	cout << "x == " << x << " p == " << p << endl;

	return 0;
}
