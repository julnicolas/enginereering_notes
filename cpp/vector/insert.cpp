#include <vector>
#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	vector<int> v = {1, 2, 5, 6};
	vector<int> v2 = {3, 4};

	v.insert(next(v.cbegin(), 2), v2.cbegin(), v2.cend());

	for (int x : v) {
		cout <<  x << endl;
	}

	return 0;
}
