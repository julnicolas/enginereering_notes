/* Delegation constructor
 * Use another same class' constructor
 * do the initialisation for another.
*/
#include <iostream>
using namespace std;

class A {
	public:
		explicit A(int i): _i(i) {}
		// A(int) is used as a delegating constructor
		// for A(int, int)
		explicit A(int i, int j): A(i + j) {}
		int i() const { return _i; }
	private:
		int _i;
};

int main(int argc, char* argv[]) {
	cout << A(1, 2).i() << endl;
	return 0;
}
