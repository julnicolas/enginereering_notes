package main

/* Explains how to define CLI flags in go.
Note - there is no automatic handling for required flags.
This is your job to check depending on provided values.

Flag value can be passed with different formats:
-fname value
--fname value
-fname=value
--fname=value

--help or -h shows help messages.

Note - to define a more elaborated help message,
it is necessary to define a new FlagSet with NewFlagSet.
With this new FlagSet override the PrintDefault function
to your liking.

*/

import (
	"flag"
	"fmt"
	"os"
	"time"
)

func main() {
	// Destination variables - they receive cli arg values
	var (
		tall     bool
		name     string
		age      uint
		someTime time.Duration
	)

	// dst var, flag name, default value, help message
	// writting --tall sets the tall flag to true, ommiting the value leave it to false
	flag.BoolVar(&tall, "tall", false, "whether the person is tall or not")
	flag.StringVar(&name, "name", "", "person's name [required]")
	flag.DurationVar(&someTime, "time", time.Second, "some duration for the example")
	flag.UintVar(&age, "age", 0, "person's age")

	// Parse the values to populate destination variables
	flag.Parse()

	// Validation code
	if name == "" {
		fmt.Println("error - empty name value")
		// Print help message
		flag.PrintDefaults()
		os.Exit(1)
	}

	// Your app code
	msg := fmt.Sprintf(`Hello my name is %s!
I am %d years old, apparently rather %s.
Also it is %v on my watch now.

Cheers!`, name, age, tallOrSmall(tall), someTime)

	fmt.Println(msg)
}

// tallOrSmall returns "tall" if tall is true "small" otherwise
func tallOrSmall(tall bool) string {
	if tall {
		return "tall"
	} else {
		return "small"
	}
}
