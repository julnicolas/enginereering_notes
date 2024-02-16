package main

import "fmt"

// Checks if the channel is closed while reading
func main() {
	// avoid locking as I'll stay in main go routine
	c := make(chan int, 1)
	c <- 1

	// channel is open so
	// v == 1 and ok == true
	v, ok := <- c
	fmt.Println(v, ok)

	// now it's closed so
	// v == 0 and ok == false
	close(c)
	v, ok = <- c
	fmt.Println(v, ok)
}
