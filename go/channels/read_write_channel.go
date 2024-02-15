package main

// Simple code scenario to show how to read and write
// from an unbuffered channel in go.
//
// see buffered_chan note for more details on the
// difference between a buffered and non-buffered
// chan

import (
	"time"
	"fmt"
)

func sum(c chan int) (result int) {
	// Waits until chan is closed
	for i := range c {
		fmt.Printf("sum: received %d\n", i)
		result += i
	}
	// reading from a closed channel
	// exits immediatly returning
	// type's zero value
	zero := <- c
	fmt.Printf("sum: read after close == %d\n", zero)
	fmt.Println("sum is over")
	return
}

func main() {
	// unbuffered channel
	c := make(chan int)
	ints := []int{2, 4, 6}

	// Start sum func
	// To store results use a dedicated
	// struct with sum being a method
	// to avoid concurrency issues
	go sum(c)

	// Populate ints
	for _, n := range ints {
		fmt.Printf("sending %d\n", n)
		c <- n
	}
	// So that sum can stop waiting
	fmt.Println("closing chan")
	// if called from another function,
	// defer close(c) should be called instead
	close(c) 
	// writing to a closed channel causes a panic
	//c <- 120

	// So that sum has time to return
	// Note - waitgroups can be used for similar scenarios
	// Though I want to emphasize on chans' behaviour
	fmt.Println("waiting 2s")
	time.Sleep(2*time.Second)
	fmt.Println("main is over")
}
