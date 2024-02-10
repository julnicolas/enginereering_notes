package main

import "fmt"

// This is how to define type aliases in go
// Type aliases can be interverted seemlessly
// They are synonyms

type myuint32 = uint32

// This defines a different type based on uint32
type u32 uint32

func PrintMyUint32(i myuint32) {
	fmt.Printf("PrintMyUint32 - %d\n", i)
}

func PrintU32(i u32) {
	fmt.Printf("PrintMyUint32 - %d\n", i)
}

func main() {
	PrintMyUint32(uint32(1))
	PrintMyUint32(myuint32(1))
	PrintU32(u32(2))
	// Compile error
	// uncomment for details
	//PrintU32(uint32(2))
}
