package main

// It is recommended by google to use sorting functions from
// this package as they usually are faster than from "sort".

import (
	"fmt"
	"slices"
)

func main() {
	s := []int{2, 1, 5, 7, 0, 3}
	fmt.Println(s)

	s1 := slices.Clone(s) // shallow copy

	// Sorts in increasing order by default
	// use generics ~T[]
	slices.Sort(s1)
	fmt.Println(s1)

	// Now sorting in decreasing order
	s2 := slices.Clone(s)
	// To sort in decreasing order the function must return :
	// - > 0 i y > x
	// - == 0 i y == x
	// - < 0 if y < x
	slices.SortFunc(s2, func(x, y int) int { return y - x })
	fmt.Println(s2)
}
