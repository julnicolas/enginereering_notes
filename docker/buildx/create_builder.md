# Create a docker builder
Docker builders rely on `BuildKit`.

To create a new builder for one or several platforms:
``` sh
docker buildx create \
--name arm-amd-64 \
--platform linux/amd64,linux/arm64 [--use]
```
`--use` tells the docker engine to use the newly created
builder as default.

