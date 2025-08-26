package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	fmt.Println(now)
	fmt.Printf("%v\n", now.Add(5*time.Minute))
	fmt.Println(now.Add(-2 * time.Minute))
}
