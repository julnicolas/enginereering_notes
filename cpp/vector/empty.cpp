// Returns true if empty
#include <vector>
#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	vector<int> v;
	if (v.empty()) {
		cout << "empty" << endl;
	}

	v.push_back(1);
	if (!v.empty()) {
		cout << "not empty" << endl;
	}

	return 0;
}
