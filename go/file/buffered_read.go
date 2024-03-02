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
    f.Close()

    var line string
    r := bufio.NewScanner(f)
    for r.Scan() {
        line = r.Text()
        fmt.Println(line)
    }

    if err := r.Err(); err != nil {
        logrus.Errorln(err)
        os.Exit(1)
    }
}
