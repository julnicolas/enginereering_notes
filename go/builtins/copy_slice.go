package main

import "fmt"

/* Copies a source slice to a destination slice.
Memory region can overlap (similar to a memmove in C).

As a special case, can copy a slice of bytes to a string.
*/

func main() {
	v := []int{1, 2, 3, 4}
	v2 := make([]int, 2)
	copy(v2, v[:2])
	fmt.Println(v, v2)
}
