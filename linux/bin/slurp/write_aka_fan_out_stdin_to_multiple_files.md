# Fan out stdin to several files

``` sh
echo 'hello' | slurp foo bar
```

Will write hello to `foo` and `bar`.
Both files will be *overwritten* if
they already existed.

