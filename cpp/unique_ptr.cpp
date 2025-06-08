// This code shows how to use unique pointers
#include <cinttypes>
#include <iostream>
// include this for std::move and ptr types
#include <memory>

using namespace std;

struct Buffer {
	uint8_t _buffer[100];	
};

// As one can see below, no explicit new or delete have to be made.
// Memory is automatically deallocated when exiting scope.
// This follows RAII principle, it is close to rust's ownership
// logic as well - when exiting scope, value is dropped.
int main(int argc, char* argv[]) {
	unique_ptr<Buffer> buffer; // nullptr
	if (!buffer) {
		cout << "no buffer has been allocated yet" << endl;
	}

	{
		buffer = make_unique<Buffer>();
		if (buffer) {
			cout << "buffer is allocated" << endl;
		}

		auto move_ownership_ptr = std::move(buffer);
		if (move_ownership_ptr) {
			cout << "ownership of buffer transfered" << endl;
		}

		cout << "exiting scope" << endl;
	}

	if (!buffer) {
		cout << "buffer has been deallocated" << endl;
	}
	return 0;
}
