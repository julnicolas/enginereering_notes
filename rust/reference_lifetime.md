# Lifetime Rules

In rust, to avoid dangling references, every
reference is assigned a lifetime.

A lifetime specifies until what scope the reference
is valid for the compiler's `borrow checker` to assess
whether the reference is dangling or not.

There is a specific lifetime that runs for the whole
duration of the program, this is the `'static` lifetime.

Lifetimes are declared as generic types, though with a leading
quote.

Example:
``` rs
fn longuest<'a>(str1: &'a str, str2: &'a str) -> &'a str {
    if str1 > str2 {
        str1
    } else {
        str2
    }
}
```

It is not always necessary to specify lifetimes as the compiler
will use three rules to determine lifetimes. If there some ambiguities,
then it issues an error, forcing programmers to specifiy the lifetimes to
remove ambiguity.

These three rules are:
- The first rule is that the compiler assigns a lifetime parameter to each parameter that’s a reference. In other words, a function with one parameter gets one lifetime parameter: fn foo<'a>(x: &'a i32); a function with two parameters gets two separate lifetime parameters: fn foo<'a, 'b>(x: &'a i32, y: &'b i32); and so on.

- The second rule is that, if there is exactly one input lifetime parameter, that lifetime is assigned to all output lifetime parameters: fn foo<'a>(x: &'a i32) -> &'a i32.

- The third rule is that, if there are multiple input lifetime parameters, but one of them is &self or &mut self because this is a method, the lifetime of self is assigned to all output lifetime parameters. This third rule makes methods much nicer to read and write because fewer symbols are necessary.

Finally, some programming pattern are added to the compiler, if your function fit that patterns then a lifetime
specification is not necessary. This is called `lifetime ellision`. These patterns are added over time by analysing
common rust code patterns.

