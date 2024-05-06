package main

import "fmt"

// Deletes an item from a map

func main() {
	m := map[string]int{"a": 1, "b": 2}

	fmt.Println(m)
	delete(m, "a")
	fmt.Println(m)
}
