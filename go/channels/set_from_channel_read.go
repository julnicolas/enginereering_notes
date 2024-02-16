package main

// Shows how to set a new variable from a channel

import "fmt"

func main() {
	c := make(chan int, 1) // to avoid locking
	defer close(c)
	
	c <- 1
	i := <- c
	fmt.Println(i)
}
