package main

import (
	"flag"
	"os"
	"fmt"
)

// CustomUsage defines a custom help message
func CustomUsage() {
	header := fmt.Sprintf("%s is a small program greeting someone politely\n",
	os.Args[0])

	fmt.Fprintf(flag.CommandLine.Output(), header)
	flag.PrintDefaults()
}

func main() {
	flag.Usage = CustomUsage

	var name string
	flag.StringVar(&name, "name", "", "person's name")
	flag.Parse()

	// verification
	if name == "" {
		fmt.Println("error - name cannot be empty")
		flag.Usage() // print usage/help message
		os.Exit(1)
	}

	fmt.Printf("Hello %s! \n", name)
}
