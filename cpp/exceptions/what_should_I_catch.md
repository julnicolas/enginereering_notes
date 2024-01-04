# What should I catch
`Source isocpp.org`

In keeping with the C++ tradition of “there’s more than one way to do that”
(translation: “give programmers options and tradeoffs so they can decide 
what’s best for them in their situation”), C++ allows you a variety 
of options for catching.

- You can catch by value.
- You can catch by reference.
- You can catch by pointer.

In fact, you have all the flexibility that you have in declaring function parameters,
and the rules for whether a particular exception matches (i.e., will be caught 
by) a particular catch clause are almost exactly the same as the rules for 
parameter compatibility when calling a function.

Given all this flexibility, how do you decide what to catch? Simple: 
unless there’s a good reason not to, catch by reference. Avoid 
catching by value, since that causes a copy to be made and the copy 
can have different behavior from what was thrown. Only under very special
circumstances should you catch by pointer.

## Example
``` cpp
try {
    //...
}
catch (std::exception& e) {
    cerr << e.what() << endl;
}
```

