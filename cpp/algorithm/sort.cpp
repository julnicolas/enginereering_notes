#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

void print(const vector<int>& vv) {
	cout << "[ ";
	for (auto v : vv) {
		cout << v << ", ";
	}
	cout << "]" << endl;
}

int main(int argc, char* argv[]) {
	vector<int> vv = {4, 3, 1, 15, 23, 2};
	auto v2 = vv;

	sort(vv.begin(), vv.end());
	print(vv);
	
	sort(vv.begin(), vv.end(), [](int x, int y){ return x > y; } );
	print(vv);

	print(v2);
	sort(v2.begin(), v2.end(), greater<int>() );
	print(vv);

	return 0;
}
