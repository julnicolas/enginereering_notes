# Vpointers and Vtables

When functions to be called can be determined at runtime, this is called `static dispatch`.
When, conversely, it happens at runtime then it is called `dynamic dispatch`.

Dynamic dispatch is used for `virtual functions` only. Called functions depend on the
type of the object. It is determined at runtime. This happens when covariant (polymorpic) 
types are passed as input parameter functions.

``` cpp
std::string g(const A& a) {
    // Call either A::f or B::f depending if
    // a is of type A or B where B is a subclass
    // of A and f a virtual method
    return a.f();
}
```

To be able to implement dynamic dispatch, every class with `virtual` functions
contain a `virtual table` containing all virtual function addresses.

Subclasses' virtual tables contain their classe's `overriden` methods as well
as inherited parent class's methods. Overriden methods, `overriding` parents'
entries in the subclasses' virtual table.

This implementation enables to centralise the table for all objects of a same
class. Hence saving memory.

However, the compiler needs to determine what table to refer to at compile time
to call the right function but, the type of the object will only be known at runtime!
That means the compiler cannot take this decision and must leave it to the object.
The way to enable it is to add to every objects instantiating a class with
virtual functions, a pointer to the object's class virtual table. This pointer is
called the `virtual pointer` - pointer to the virtual table.

Please see below equivalent cpp code to the compiler's assembly translation:
``` cpp
std::string g(const A& a) {
    // return a.vpointer[index_of_f]()
    return a.f();
}
```

