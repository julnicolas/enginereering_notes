# Show Race Conditions
Build a binary with code tracking race conditions.
Expect a speed degradation as well as an increased
memory usage.

``` sh
go build -race -o foo main.go
```

