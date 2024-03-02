// Buffered read
package main

import (
    "bufio"
    "fmt"
    "os"

    "github.com/sirupsen/logrus"
)

// Reads a file line per line
func main() {
    f, err := os.Open("filename")    
    if err != nil {
        logrus.Errorln(err)
        os.Exit(1)
    }
    defer f.Close()

    var line string
    r := bufio.NewScanner(f)

	// Returns False when EOF has been reached
	// If it has been reached once but then the file has content added to it
	// again then, Scan will still return False.
	//
	// Therefore to tail a file one of the aspect to keep in mind is to check the amount
	// of read bytes... given the file hasn't been overwritten! It is preferable to use the
	// tail package for that effect then.
    for r.Scan() {
        line = r.Text()
        fmt.Println(line)
    }

    if err := r.Err(); err != nil {
        logrus.Errorln(err)
        os.Exit(1)
    }
}
