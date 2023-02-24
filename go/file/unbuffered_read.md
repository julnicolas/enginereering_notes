# Unbuffered read
``` go
package main

import (
    "fmt"
    "io"
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

    content := io.ReadAll(f)
    fmt.Println("now printing all", content)
}
```
