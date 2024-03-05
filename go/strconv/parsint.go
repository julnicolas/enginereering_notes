package main

import (
	"fmt"
	"strconv"
)

// Shows how to parse an int
func main() {
	// Returns an int, base 10 assumed
	i, err := strconv.Atoi("123")
	if err != nil {
		panic(err)
	}
	fmt.Println(i)
	// Returns an int64
	// first arg: str to convert
	// base in use, if 0 use string prefix to deduce, no prefix -> 10
	// last param: bit size parsed int must fit into
	//  i.e. if parsed bit is 64-bit long but expected bit size is 32 then
	//  an error is returned
	j, err := strconv.ParseInt("A", 16, 64)
	if err != nil {
		panic(err)
	}
	fmt.Println(j)
}
