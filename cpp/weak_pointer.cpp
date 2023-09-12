/* Weak pointers represent memory addresses which can be deallocated at
 * all times by another party.
 *
 * Weak pointers are converted into shared pointers when accessing a memory address.
 *
 * Note: weak pointers can also be used to break shared pointer dependency cycles.
*/

#include <memory>
#include <iostream>
#include <cassert>

using namespace std;

int main(int argc, char* argv[]) {
	weak_ptr<int> w; // pointer is empty, underlying ptr is nullptr
	{
		shared_ptr<int> s = make_shared<int>(2);
		w = s; // assignment operator of weak from shared ptr

		// Creates a new shared pointer from the address contained in the weak
		// pointer. Said pointer will point to allocated memory if shared pointer
		// is still valid (how can it be determined?). If not, the shared pointer
		// is empty.
		//
		// shared pointers and unique pointers convert to bool: true means the pointer
		// is not nullptr, false otherwise.
		//
		// Note: if reference base pointer is deallocated right after the lock is aquiered,
		// the object's lifetime is prolongated as a new shared pointer has been created.
		if (auto ws = w.lock()) { 
			cout << "*weak ptr == " << *ws << endl;
		}
	}

	// Here, the shared pointer has been deallocated so memory address contained in the weak
	// pointer is not valid anymore. Value of static_cast<bool>(w.lock()) should be false.
	assert(static_cast<bool>(w.lock()) == false);
	cout << "weak pointer is empty" << endl;

	// Another way of using a weak pointer's content, that is to convert it to a shared pointer,
	// is to construct a shared pointer by copy from a weak pointer (instead of copy assigning a
	// shared pointer to a weak pointer).
	//
	// The only difference when copy constructing is that if copy construction cannot be carried
	// out then an expression is thrown (if weak_ptr's lock can be evaluated to false).
	try {
		shared_ptr<int> s(w);
	}
	catch (bad_weak_ptr& e) {
		cerr << "weak pointer is empty, exception: " << e.what() << endl;
	}

	return 0;
}
