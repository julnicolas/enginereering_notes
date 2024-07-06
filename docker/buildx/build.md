# Build with buildx
Make sure you `docker buildx use` your builder first.

If the platform you're building form has a different architecture,
make sure you have `QEMU` installed. This is used by default by `BuildKit`.

``` sh
docker buildx build --platform linux/arm64,linux/amd64 -t my_container .
```
Note - `--platform` is available on the default `build` command. However,
only one architecture can be chosen at a time.

