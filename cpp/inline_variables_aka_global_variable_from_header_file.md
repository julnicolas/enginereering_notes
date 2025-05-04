# Inline variables - global variable from header files

For a variable to be available to another compilation unit (.o), it must
have `external` linkage. The related keyword can be used in either `.h`
or `.cpp` files. It's just a matter whether the developper wants to make
it easy for other devs to know such variable exists or not. Indeed,
if external is only used in cpp files, as the binary is compiled,
this info will certainly lost by the user (generally only headers are vendored).

## C++ 17 and later

``` cpp
# In .h
# This variable will be accessible as foo::c
namespace foo {
    inline Myclass c;
}
```

That's it. No definition is necessary in the cpp file.

## Older c++
### .h and .cpp

``` cpp
# In .h
namespace foo {
    extern Myclass c;
}

# In .cpp
#include <foo.h>

namespace foo {
    Myclass c;
}
```

### Cpp only

Make sur to compile foo.cpp and main.cpp so that
the linker looks up in the generated foo.o for
the the `external` variable `i`.

``` cpp
# In foo.cpp

namespace foo {
    int i = 42;
}

# In main.cpp
#include <iostream>
using namespace std;

namespace foo {
    extern int i;
}

int main(int argc, char* argv[]) {
    cout << i << endl;
    return 0;
}
```

