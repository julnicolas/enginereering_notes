// Returns an iterator at index i+1 (ith value)
//#include <iterator> // just to get std::next
#include <vector>
#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	vector<int> v = {1, 2, 3, 4, 5};
	auto it = next(v.cbegin(), 2);

	cout << *it << endl;

	return 0;
}
