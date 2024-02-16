package main

/* This program shows how to pass channels
to functions but specifying only one of read
or write direction (sending or receiving end).

It is better to specify it so that compiler can
help prevent unintended behaviours.

*/

import "fmt"

// ReadWrite can both read and write to channel c
func ReadWrite(c chan int) {}

// ReadOnly receives a read only chan and reads its content
func ReadOnly(c <-chan int) {
	for i := range c {
		fmt.Printf("received %d\n", i)
	}
}

// Type used to signal waiting for channels is over
// Only one value is possible - StopSignal{}
type StopSignal struct{}

// WriteOnly receives two write only channels
// It first writes content to c, then when over,
// sends to StopSignal
func WriteOnly(c chan<- int, stop chan<- StopSignal) {
	ints := []int{2, 4, 6}
	for _, v := range ints {
		fmt.Printf("writing %d\n", v)
		c <- v
	}

	stop <- StopSignal{}
}

func main() {
	c := make(chan int)
	stop := make(chan StopSignal)

	go ReadOnly(c)
	go WriteOnly(c, stop)
	<- stop
}
