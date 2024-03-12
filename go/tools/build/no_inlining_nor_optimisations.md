# Disable Inlining and Optimisations
``` sh
go build -gcflags '-N -l' -o foo main.go
```

