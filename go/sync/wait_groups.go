package main

// Shows how to use a waitgroup

import (
	"fmt"
	"sync"
	"time"
)

// Print prints a message then wait a second before terminating
func Print(i int, wg *sync.WaitGroup) {
	fmt.Println("printing", i)
	time.Sleep(time.Second)

	// When work is done, decrement wait count
	// so that main go routine in our example is
	// not waiting for ever
	//
	// Done should be the last statement run by a waitable
	// task
	wg.Done()
}

func main() {
	wg := &sync.WaitGroup{}
	for i := 0; i < 5; i++ {
		// make sure to increment wait counter from waiting routine
		// to prevent race conditions
		wg.Add(1)
		go Print(i, wg)
	}
	wg.Wait()
	fmt.Println("finished main exec, should have printed 5 messages")
}
