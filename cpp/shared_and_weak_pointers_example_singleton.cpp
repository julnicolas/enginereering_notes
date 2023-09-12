#include <memory>
#include <iostream>
#include <exception>
#include <cassert>

using namespace std;

class NULLSingletonError: public exception {
	public:
		const char* what() const noexcept override {
			return "error - singleton is being accessed whereas not allocated; ";
		}
};

class Singleton {
	public:
		static void create();
		static void destroy();
		static weak_ptr<Singleton> get();

		void f() const;

		// Destructor must be public so that shared_ptr
		// can destruct on shared_ptr reset.
		~Singleton();
		Singleton(const Singleton&) = delete;
		Singleton(Singleton&&) = delete;
		Singleton& operator=(const Singleton&) = delete;
		Singleton& operator=(Singleton&&) = delete;

	private:
		// constructor must be private so that only one instance can be
		// allocated and only from the static function.
		//
		// Then allocation is made calling new from the static function
		// (as shared_ptr<Singleton> cannot allocate as the constructor is
		// private)
		Singleton() = default;

		static shared_ptr<Singleton> _self;
};

Singleton::~Singleton() {
	cout << "Singleton's destructor" << endl;
}

// Has to be initialised before static functions are called
shared_ptr<Singleton> Singleton::_self;

void Singleton::create() {
	// equivalent to (_self != nullptr)
	if (!_self) {
		// if class constructor is public:
		// _self.reset();
		_self.reset(new Singleton);
	}
}

void Singleton::destroy() {
	if (_self) {
		// Calls destructor here, _self will be empty after this
		_self.reset();
	}
}

weak_ptr<Singleton> Singleton::get() {
	if (!_self) {
		throw NULLSingletonError();
	}
	
	return _self;
}

void Singleton::f() const {
	cout << "this is from f" << endl;
}

int main(int argc, char* argv[]) {
	Singleton::create();

	auto weak = Singleton::get();
	// Syntax to use when calling the singleton
	//auto s = Singleton::get().lock();
	{
		// For the example the weak pointer is saved so that it can
		// be used latter on on a bad test and shared pointer and pointed
		// object can be deallocated
		auto s = weak.lock();
		if (s) {
			s->f();
		}
	}

	Singleton::destroy();
	try {
		Singleton::get();
	}
	catch (NULLSingletonError& e) {
		cerr << e.what() << endl;
	}

	cout << "checking weak pointer is empty" << endl;
	assert(!weak.lock());
	cout << "DONE." << endl;

	return 0;
}
