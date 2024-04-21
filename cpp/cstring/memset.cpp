// Set byte value to whole buffer
// byte-per-byte

#include <cstring>
#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	int b[8];
	memset(b, 0, sizeof(b));

	for (int i = 0; i < 8; i++) {
		if (b[i] != 0) {
			cout << "error" << endl;
		}
	}

	return 0;
}
