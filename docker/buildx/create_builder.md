# Create a docker builder

Docker builders rely on `BuildKit`.
Before creating the builders, make sure the right emulators are installed.

## Install emulators
``` sh
pacman -S qemu-user-static
sudo docker run --privileged --rm tonistiigi/binfmt --install all
```

The docker image installs the qemu emulators. It sets them up so that they are
recognizable by `BuildKit` using `binfmt`.

They are installed in `/proc/sys/fs/binfmt_misc`.

To check emulator status run the above docker run command again.

## Create a new builder

To create a new builder for one or several platforms:
``` sh
docker buildx create \
--name buildkit \
--driver docker-container \
--platform linux/amd64,linux/arm64 [--use]
```
`--use` tells the docker engine to use the newly created
builder as default.

Note - I use `buildkit` as argument to `--name` but it can be anything.

## Gotchas
Note - even doing as above, some commands may fail. Installing
poetry fails emulating an arm64 platform on amd64 as the cffi module
needs to be recompiled. For that to be completed, some additionnal packages
needed to be installed.

