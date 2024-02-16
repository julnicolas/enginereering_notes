package main

// Shows how to set a new variable from a channel

import "fmt"

func main() {
	// to avoid locking as I'm staying in
	// the main go routine
	c := make(chan int, 1)
	
	c <- 1
	i := <- c
	fmt.Println(i)
}
