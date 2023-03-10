package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("printing every seconds, 5 times")
	tick := time.Tick(time.Second)

	var i int
	for range tick {
		fmt.Println("tick")
		i++

		if i == 5 {
			break
		}
	}
}
