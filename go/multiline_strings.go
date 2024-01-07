package main

// Shows how to define a multiline string with
// backticks.

import "fmt"

func main() {
	str := `This is
multiline
string
	aka a raw string.`

	fmt.Println(str)
}
