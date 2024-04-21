// Compare two buffers in lexicographic order
#include <cstring>
#include <iostream>

using namespace std;

inline size_t min(const size_t x, const size_t y) {
	return x < y ? x : y;
}

int main(int argc, char* argv[]) {
	const char* b1 = "hello";
	const size_t l1 = strlen(b1);

	const char* b2 = "bonjour";
	const size_t l2 = strlen(b2);

	if (memcmp(b1, b2, min(l1, l2)) < 0) {
		cout << "smaller" << endl;
	} else {
		cout << "higher or equal" << endl;
	}

	return 0;
}
