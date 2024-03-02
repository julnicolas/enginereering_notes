package main

import (
	"fmt"
	"os"
)

// Shows how to read argv in go
func main() {
	for _, arg := range os.Args {
		fmt.Println(arg)
	}
}
