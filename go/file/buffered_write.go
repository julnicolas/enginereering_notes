// Buffered write
package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"

    "github.com/sirupsen/logrus"
)

// Writes content to file, buffering the output
func main() {
    f, err := os.OpenFile("file_path", os.O_CREATE | os.TRUNC | os.WRONLY, 0644)
    if err != nil {
        logrus.Errorln(err)
        os.Exit(1)
    }
    defer f.Close()

    data := strings.Fields("some data to send over")

    var err error
    w := bufio.NewWritter(f)
    for _, d := range data {
        _, err = w.WriteString(d) // can use fmt.Fprintf
        if err != nil {
            logrus.Errorln(err)
            os.Exit(1)
        }
    }

    // Call flush to make sure all bytes make it to the file
    w.Flush()
}
