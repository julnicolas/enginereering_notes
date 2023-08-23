// Shows how to use shared pointers in a program
#include <memory>
#include <iostream>
#include <string>

using namespace std;

class Foo {
	public:
		Foo(shared_ptr<string> s): m_s(s) {}
		string str() { return *m_s; }

		~Foo() = default;
		Foo(const Foo&) = default;
		Foo(Foo&&) = default;
		Foo& operator=(const Foo&) = default;
		Foo& operator=(Foo&&) = default;

	private:
		shared_ptr<string> m_s;
};

int main(int argc, char* argv[]) {
	// Mandatory to create an object whose address will be reference
	// counted by shared_ptr.
	//
	// Shared pointers must be passed by copy so that reference count can
	// be incremented during copy, decremented during deletion.
	//
	// The last destruction destroys the shared object (calls delete)
	auto p = make_shared<string>("hello world");
	Foo foo(p);

	cout << foo.str() << endl;

	return 0;
}
