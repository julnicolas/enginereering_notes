# Lookup exported symbols in C/CPP static library (.a)
`nm` comes with GNU development tools.

``` sh
nm -C $LIB_PAT
```

Note: `-C` is optional, it demangles symbols

