package main

// Shows how to use a mutex

import (
	"fmt"
	"time"
	"sync"
)

var mutex sync.Mutex

func read(s [3]int) {
	mutex.Lock()
	defer mutex.Unlock()

	for _, i := range s {
		fmt.Printf("read %d\n", i)
	}
}

func write(s [3]int) {
	mutex.Lock()
	defer mutex.Unlock()

	for i := range s {
		s[i] += 1
		fmt.Println("write", i)
	}
}

func main() {
	s := [3]int{0, 1, 2}
	for i := 0; i < 3; i++ {
		go write(s)
		go read(s)
	}

	fmt.Println("waiting 3s")
	time.Sleep(3*time.Second)
	fmt.Println("done")
}
