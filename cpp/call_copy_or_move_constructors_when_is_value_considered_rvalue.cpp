/* shows various cases of copy constructor and 
 * move constructor invovations
 */

#include <string>
#include <iostream>

using namespace std;

class str {
	public:
		str(const char* s): _s(s) { cout << "constructor -> "; }
		str(const str& s): _s(s._s) { cout << "copy constructor -> "; }
		// in order to call this constructor an rvalue must be returned
		// - a rvalue is an explicit returned rvalue reference
		// - a litteral
		// - a std::move lvalue or lvalue reference
		// Important - do not reuse a variable that has been moved!
		// a move operation is equivalent to a change of ownership.
		// Therefore, moved object state cannot be guaranteed.
		str(str&& s): _s(move(s._s)) { cout << "move constructor -> "; }

		friend ostream& operator<<(ostream& s, const str& str) {
			return s << str._s;
		}
	private:
		std::string _s;
};

int main(int argc, char* argv[]) {
	str s = "hello";
	cout << "s == " << s << endl
		<< "-------" << endl;

	str s1(s);
	cout << "s1 == " << s1 << endl
		<< "-------" << endl;

	cout << "rvalue? == " << str(s) << endl
		<< "-------" << endl;
	cout << "rvalue2? == " << str("bonjour") << endl
		<< "-------" << endl;
	cout << "rvalue3? == " << str(move(s)) << endl
		<< "s cannot be used from here as ownership" 
		<< " as changed due to move construction" << endl
		<< "-------" << endl;
	// s cannot be used from here

	return 0;
}
