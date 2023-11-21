# Copy Ellision
Copy ellision is a compiler optimisation when the compiler will eventually
skip copy operations without impacting programs' correcteness.

Said differently, it will remove redundant copy operations from copy constructors.

Copy ellision is a standardized optimisation. For optimisation details please check:
https://en.cppreference.com/w/cpp/language/copy_elision 

``` cpp
void f(A);
A A::operator+(const A&);

A a;
f(a); // A's copy constructor is called
// Copy constructs the result of a + a
// Copy constructs anoter object to pass
// to f as a copy of a + a 
// -> this copy is redundant, it can be ommited
// the ommition is a copy ellision.
f(a + a);
```

