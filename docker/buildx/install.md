# Install buildx plugin
`docker buildx` uses `BuildKit` as image build backend.
Perks include build parrallelisation and multi-cpu-architecture support.

On archlinux install:
``` sh
pacman -S docker-buildx
```

