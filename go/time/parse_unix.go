package main

import (
	"fmt"
	"time"
)

func main() {
	// Unix time in seconds, 0 nano seconds
	// returns a time.Time object
	t := time.Unix(1405544146, 0)
	fmt.Println(t)
}
