#include <iostream>

/* This program presents a technique for tagging
 * functions so that a specialised form (with
 * related semantics) can be used with no
 * overhead.
 *
 * Tagging is a technique for calling a specialised
 * version of a function at compile time by providing
 * a named-empty-type so that the compiler can choose
 * the appropriate specialisation.
 *
 * Here I used an empty shell class so that type information
 * can be provided at name-resolution level to not clutter
 * function parameters (and pass empty parameters on the stack). 
 */

namespace logging {
	// Supported log levels
	using info = struct {};
	using warning = struct {};
	using error = struct {};
			
	
	template <typename T>
	class logger {
		public:
			// Useful if passed in a templated expression
			using level = T;

			// Prevent class instantiation so that
			// it is just a name-spaced shell that
			// contains functions
			//
			// It allows the log function to be
			// type-parametered (tagged) without the
			// introduction of an empty parameter passed
			// on the stack.
			static void log(const char* msg);

			logger() = delete;
			~logger() = delete;
			logger(const logger&) = delete;
			logger(logger&&) = delete;
			logger& operator=(const logger&) = delete;
			logger& operator=(logger&&) = delete;
	};
	
	// Unsupported log levels trigger a compilation error
	template <typename T>
	void logger<T>::log(const char* msg) {
		using not_implemented = struct {};
		static_assert(not_implemented{});
	}
	
	template <>
	void logger<info>::log(const char* msg) {
		std::cout << "info - " << msg << std::endl;
	}
		
	template <>
	void logger<warning>::log(const char* msg) {
		std::cout << "warning - " << msg << std::endl;
	}
		
	template <>
	void logger<error>::log(const char* msg) {
		std::cerr << "error - " << msg << std::endl;
	}
}

int main(int argc, char* argv[]) {
	using namespace logging;

	logging::logger<logging::info>::log("hello");
	logger<warning>::log("world");
	logger<error>::log("danger");

	return 0;
}
