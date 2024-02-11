package main

import "fmt"

/*
Builtins constraints are the following:
- any (defined in builtins.go as type any = interface{})
- comparable (defined in builtins.go as type comparable = interface{ comparable })
	comparable types are compatible with <, >, and == operators
- any type defined in the 'constraints' package. It defines:
	- numeric types such as Int for ~int | ~int8 | ~int16 ... 
	- the Ordered type which refers to types having < and > operator
	  but not necessarily the == operator.
*/

// Any returns true if at least one entry in s1 verifies the predicate
func Any[T comparable](s []T, pred func(T)bool) bool {
	result := false
	for _, item := range s {
		result = result || pred(item)
	}
	return result
}

func main() {
	res := Any([]int{1, 2, 3}, func(x int)bool{ return x >= 4 })
	fmt.Println(res)

	res = Any([]int{1, 2, 3, 4}, func(x int)bool{ return x < 4 })
	fmt.Println(res)

	res = Any([]string{"hi", "hello", "hola"}, func(x string)bool{ return x == "hola" })
	fmt.Println(res)
}
