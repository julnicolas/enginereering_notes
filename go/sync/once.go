package main

// Once.Do execute a function only once even
// if called concurently from other go routines

import (
	"fmt"
	"time"
	"sync"
)

func UniqueMsg() {
	fmt.Println("Unique Message")
}

func Msg(i int) {
	fmt.Println("Msg", i)
}

func Print(i int, once *sync.Once) {
	once.Do(UniqueMsg)
	Msg(i)
}

func main() {
	once := &sync.Once{}
	for i := 0; i < 5; i++ {
		go Print(i, once)
	}
	// Leave time to go routines to terminate
	fmt.Println("main: sleeping for 2s")
	time.Sleep(2*time.Second)
}
