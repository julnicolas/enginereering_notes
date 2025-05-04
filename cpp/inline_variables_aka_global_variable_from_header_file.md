# Inline variables - global variable from header files

This feature is available from `c++ 17`:

``` cpp
# In .h
# This variable will be accessible as foo::c
namespace foo {
    inline Myclass c;
}
```

That's it. No definition is necessary in the cpp file.

In older versions of c++:

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

