package main

import "fmt"


func main() {
	var unknown interface{} = "hello"

	// Access interface underlying type and value to check
	// type's value.
	if v, ok := unknown.(int); ok {
		fmt.Printf("this is an int of value '%d'\n", v)
	} else {
		fmt.Println("interface is not an int")
	}

	if v, ok := unknown.(string); ok {
		fmt.Printf("this is a string of value '%s'\n", v)
	}

	// The following form panics if assertion is false
	fmt.Println("panic version to access value, ", unknown.(string))
}
