# Unbuffered write
``` go
package main

import (
    "fmt"
    "os"

    "github.com/sirupsen/logrus"
)

func main() {
    f, err := os.Open("file")
    if err != nil {
        logrus.Errorln(err)
        os.Exit(1)
    }
    defer f.Close()

    somevar := "heyeheyeh hello
    fmt.Fprintf(f, "%s", somevar)
}
```
