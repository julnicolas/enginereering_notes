package main

/* This program shows how to use the select
statement to wait on different channels. */

import (
	"fmt"
	"time"
)

func write(c chan<- int) {
	ints := []int{2, 4, 6}
	for _, v := range ints {
		fmt.Printf("write: sending %d\n", v)
		c <- v
	}
}

func stopAfter(stop chan<- struct{}, dur time.Duration) {
	fmt.Println("stopAfter: sleeping...")
	time.Sleep(dur)
	fmt.Println("stopAfter: sending stop signal...")
	stop <- struct{}{}
}

func main() {
	c := make(chan int)
	defer close(c)
	stop := make(chan struct{}) 
	defer close(stop)

	go write(c)
	go stopAfter(stop, 2*time.Second)

	// This bit should be in its own function but I wanted to illustrate
	// the use of break with a label
FOR_LOOP:
	for {
		// Waits until one of the channels receive a value
		// It is possible to use the default case to do something
		// while waiting
		select {
		case i := <-c:
			fmt.Printf("received %d\n", i)
		case <- stop:
			fmt.Println("received stop signal")
			// need to use label otherwise break
			// only exits from select
			break FOR_LOOP
		// default: // to do something while waiting but no use case here
		}	
	}
}
