package main

import "fmt"

/*
Type constraints are sets of types.

They are defined with the interface keyword.
Another way to define a type constraint is, a list of
types which implements an interface (go's definition but
I prefer the mathematics definition).

To have more info on ~, read the associated note.
*/

// Only int, float32 or float64 will be accepted
// myint is a 'derivated' type, that is defined from int
// Derivated types are not accepted without using ~
type ExplicitIntOrFloat interface{ int | float32 | float64 }
// int, float32 or float64 and derivated types are accepted
type IntOrFloat interface{ ~int | ~float32 | ~float64 }
// note: type myint = int, defines an alias
// an alias is considered as being the same type by the compiler.
// It just has another. An alias is not a derivated type!
type myint int
type mymyint myint
type myfloat float64
type mymyfloat myfloat

// PrintInts prints an int or a float. It accepts any derivated types of int and float32/64
func PrintIF[T IntOrFloat](t T) { fmt.Println(t) }
// Same thing but using an anonymous constraint
func PrintIF2[T interface{ ~int|~float32|~float64 }](i T) { fmt.Println(i) }
// Shorter form of anonymous type constraint
func PrintIF3[T ~int|~float32|~float64](i T) { fmt.Println(i) }

// PrintInts prints an int or a float. No derivated types are accepted
func XPrintIF[T ExplicitIntOrFloat](t T) {fmt.Println(t)}
// Same thing but using an anonymous constraint
func XPrintIF2[T interface{int|float32|float64}](t T) {fmt.Println(t)}
// Shorter form of anonymous type constraint
func XPrintIF3[T int|float32|float64](i T) { fmt.Println(i) }

func main() {
	var (
		i int = 1
		k mymyint = 3
		f float64 = 1.0
		g mymyfloat = 1.0
	)

	// Derivated types
	PrintIF(i)
	PrintIF(k)
	PrintIF(f)
	PrintIF(g)
	// build error as string is not part of type constraint
	//PrintIF("dummy")

	// Checking behaviour is similar
	PrintIF2(i)
	PrintIF2(k)
	PrintIF2(f)
	PrintIF2(g)
	// build error as string is not part of type constraint
	//PrintIF2("dummy")

	// Checking behaviour is similar
	PrintIF3(i)
	PrintIF3(k)
	PrintIF3(f)
	PrintIF3(g)
	// build error as string is not part of type constraint
	//PrintIF3("dummy")

	// Explicit types
	XPrintIF(i)
	// build error - missing ~
	//XPrintIF(k)
	XPrintIF(f)
	// build error - missing ~
	//XPrintIF(g)
	// build error as string is not part of type constraint
	//XPrintIF("dummy")

	// Checking behaviour is similar
	XPrintIF2(i)
	// build error - missing ~
	//XPrintIF2(k)
	XPrintIF2(f)
	// build error - missing ~
	//XPrintIF2(g)
	// build error as string is not part of type constraint
	//XPrintIF2("dummy")

	// Checking behaviour is similar
	XPrintIF3(i)
	// build error - missing ~
	//XPrintIF3(k)
	XPrintIF3(f)
	// build error - missing ~
	//XPrintIF3(g)
	// build error as string is not part of type constraint
	//XPrintIF3("dummy")
}
