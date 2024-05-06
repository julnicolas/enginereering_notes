package main

import "fmt"

/* Clears a container such as a map or slice
	- for maps: all elements are deleted, resulting in an
		empty map
	- for slices: all elements up to len(v) (v being a slice)
		are set to the type's 0 value

		Note: use a smaller slice representation to reduce size
		or `copy` content to a new slice
*/

func main() {
	v := []int{1, 2, 3, 4}
	m := map[string]int{"a": 1, "b": 2, "c": 3}

	fmt.Println(v, m)
	clear(v)
	clear(m)
	fmt.Println(v, m)
}
