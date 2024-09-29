# Get revision numbers for a release

``` sh
helm history $release_name
```

A revision is a counter incremeted every time a
new release is deployed. That is when an `install`,
`upgrade` or `rollback` command is used. The first
release number is `0 + 1 = 1`.

