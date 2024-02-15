package main

/*
Channel are communication structure with a builtin locking
mechanism. Locking/blocking takes effect depending on the
operation that is carried out.

Read operation (value := <- c)
-------------------------------
Blocks when the channel is empty. That is that all values
have been read.

Warning - if the channel has been closed by the writer,
attempts to read the closed channel will return immediatly
the type's zero value

Write operation (c <- value)
----------------------------
First let us define a channel:
c := make(chan int, n)
where n is a positive integer.

n corresponds to the channel's buffer size, that is, the
number of values which can be stored before blocking writes.

Let us explain this in details.

n == 0
------
If n == 0, then no messages can be stored before blocking. That is
the channel will block immediatly after sending the first message.
This is the same behaviour as making a channel without mentioning the
buffer size.
Therefore make(chan int) is equivalent to make(chan int, 0)

n == 1
------
If n == 1, then one value can be stored before blocking. That is,
the channel will save the first value, then block after writing the second.

Based on that observation, n-buffered channels block after the n+1 has been
written (if n == 0 it blocks after the first message has been written, which
is coherent with what we said earlier).

*/

import (
	"fmt"
	"time"
)

func readc(c chan int, stop chan struct{}) (err error) {
	// unlock main function when reading is over
	defer func() { stop <- struct{}{} }()

	// Initial wait to leave time to writter to lock
	// so that we can observe this behaviour
	fmt.Println("readc: initial wait of 2s")
	time.Sleep(2*time.Second)

	// read while chan is open
	// though leave time for writter
	// to lock channel.
	//
	// There is locking (waiting) if channel
	// is not closed and channel content is empty
	for i := range c {
		fmt.Printf("readc: received %d\n", i)
		fmt.Println("readc: now waiting 2s")
		time.Sleep(2*time.Second)
	}
	fmt.Println("readc: finished")
	return
}

func writec(c chan int) (err error) {
	// close channel when all rights are done
	// so that readers are not locked
	defer close(c) 

	ints := []int{2, 4, 6, 8, 10, 12, 14, 16}
	for _, v := range ints {
		fmt.Printf("sending %d\n", v)
		c <- v
	}
	return
}

func main() {
	// blocks after 1 write
	//c := make(chan int)
	// blocks after 1 write
	// equivalent to unbuffered chan
	c := make(chan int, 0)
	// blocks after 2 writes
	//c := make(chan int, 1)
	// blocks after 3 writes
	//c := make(chan int, 2)


	// value is an anonymous struct as value
	// is not important, this is just a signal.
	// we leave the compiler optimise the lighest
	// value to send.
	stop := make(chan struct{})
	go writec(c)
	go readc(c, stop)
	
	fmt.Println("waiting stop signal")
	<- stop
	fmt.Println("end of main")
}
