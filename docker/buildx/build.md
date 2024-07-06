# Build with buildx
Make sure you `docker buildx use` your builder first.

If the platform you're building form has a different architecture,
make sure you have `QEMU` installed. This is used by default by `BuildKit`.

``` sh
docker buildx build --load --platform linux/arm64,linux/amd64 -t my_container .
```

Notes 
---
- `--platform` is available on the default `build` command. However,
    only one architecture can be chosen at a time.
- `--load` show images built with buildx in `docker image ls` listing.

