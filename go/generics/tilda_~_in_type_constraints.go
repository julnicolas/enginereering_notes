package main

// Explains how to use the ~ keyword in
// type constraint definitions

import "fmt"

type myint int

// All types deriving from int are allowed
// Deriving means either defined with:
// type foo = int
// type foo int
//
// The following bar type would also be accepted:
// type foo int
// type bar foo
type Ints interface {
	~int
}

type MyInts interface {
	// compiler doesn't allow ~myint.
	// Reason: underlying type is int.
	// ~ operator can only be used on base types
	// to mean any aliases or new types defined from
	// base types (i.e. type myint int) are allowed
	myint
}

type Foo struct{}
type Bar Foo
type Baz struct {
	X int
}

// Accepts all types deriving from struct{}
// I.e Foo, Bar, struct{}, and any other derivative
// Baz is Not accepted as struct{X:int} is a different
// base type
type Foos interface {
	~struct{}
}

// Accepts all derivatives of struct{X: int}
type Bazzs interface {
	~struct{X int}
}

// Prints all derivative of int
func PrintInt[T Ints](i T) {
	fmt.Println(i)
}

// Prints only myint
func PrintMyInt[T MyInts](i T) {
	fmt.Println(i)
}

// Prints all derivative of struct{}
func PrintFoos[T Foos](t T) {
	fmt.Printf("%v\n", t)
}

// Prints all derivative of struct{X: int}
func PrintBazzs[T Bazzs](t T) {
	fmt.Printf("%v\n", t)
}

func main() {
	var (
		i myint = 1
		j int = 2
	)

	// Test with ints
	// Derivative of ints
	PrintInt(i)
	PrintInt(j)
	// myint
	PrintMyInt(i)
	// Build error:
	// int does not satisfy MyInts (int missing in main.myint)
	//PrintMyInt(j)

	// Test with structs
	// derivatives of struct{}
	PrintFoos(Foo{})
	PrintFoos(Bar{})
	PrintFoos(struct{}{})
	// Compile error
	//PrintFoos(Baz{})

	// derivatives of struct{X: int}
	// T (type Baz) does not satisfy Foos
	PrintBazzs(Baz{})
	PrintBazzs(struct{X int}{})
	// Build Error:
	// T (type struct{Z int}) does not satisfy Bazzs
	// -> expected 'X int' not 'Z int'
	PrintBazzs(struct{Z int}{})
}
