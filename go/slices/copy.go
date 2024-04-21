package main

// Shows how to do a shallow copy from one slice to a new slice
// Note - for deep copies no official packages exist.
// from what I've seen from existing 3rd parties, it is overly
// complex and some types (like time.Time) are not handled well.

import (
	"fmt"
	"slices"
)

func main() {
	s := []int{1, 2, 3}

	s2 := slices.Clone(s) // shallow copy
	fmt.Println(s2)
}
