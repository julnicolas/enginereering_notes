// Find byte in buffer

#include <cstring>
#include <iostream>

using namespace std;

// To represent bytes it is more usual to use 'unsigned char*'.
// Though for commodity I used char*
int main(int argc, char* argv[]) {
	const char* buff = "hello world";
	char* ptr = (char*) memchr(buff, 'o', strlen(buff) * sizeof(char));

	cout << *ptr << endl;

	return 0;
}

