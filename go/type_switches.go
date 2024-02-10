package main

import "fmt"

func main() {
	var unknown interface{} = "hello"

	switch v := unknown.(type) {
	case int:
		fmt.Printf("int type, value == %d\n", v)
	case string:
		fmt.Printf("string type, value == %s\n", v)
	case interface{}:
		fmt.Println("empty interface")
	}
}
