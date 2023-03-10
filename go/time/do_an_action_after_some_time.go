package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("print in 3 seconds")
	after := time.After(3*time.Second)
	<- after
	fmt.Println("3 seconds have passed")
}
