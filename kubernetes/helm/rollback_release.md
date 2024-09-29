# Rollback release
``` sh
helm rollback $release $revision
```

Use `helm history $release` to get the
revision numbers associated to the release.

A revision is a counter incremeted every time a
new release is deployed. That is when an `install`,
`upgrade` or `rollback` command is used. The first
release number is `0 + 1 = 1`.

