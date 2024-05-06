package main

import "fmt"

// Shows the capacity of a slice
// Using cap with a map results in build error
// even though space can be allocated to hold elements

func main() {
	v := make([]int, 0, 2)
	fmt.Println(cap(v))
}
