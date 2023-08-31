#include <exception>
#include <iostream>

/* Exceptions are to be used for unexpected behaviours occuring at
 * run time.
 *
 * For unexpected, normally impossible to happen behaviours
 * (such as invarients condition breaks) use asserts instead.
 *
*/

class MyError: public std::exception  {
	public:
		// const keywords are important here otherwise unexpected what version can be called.
		// please check the const_override.cpp program for further information.
		virtual const char* what() const noexcept;
		virtual ~MyError() = default;
};

const char* MyError::what() const noexcept {
	return "my error";
}

int main(int argc, char* argv[]){
	try {
		throw MyError();
	}
	// Rather use MyError& instead but that's to illustrate that
	// references should be used so that polymorphism can be used 
	// to handle errors
	catch (std::exception& e) {
		std::cout << e.what() << std::endl;
	}

	return 0;
}
