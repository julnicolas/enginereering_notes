# Docker run
Starts a docker container from a built docker image.

``` sh
sudo docker run -v ~/projects/freehowling/fh_db:/repository \
-p 8080:8080
-e GCP_PK="data blob" \ 
--rm \ 
[-it|d] \
[--entrypoint /bin/sh] \
ci-image fh-python
```

- `v`: mounts a volume to the container, first part is host's path, second is container's
- `p`: open ports, first port is host's, second is container's -> easy way to do port forwarding
- `e`: define an `environment variable`
- `rm`: remove container on exit
- `it`: combination of `i` (interactive mode) and `t` (spin up a pseudo tty)
- `d`: detached mode -> container runs in the background (parent process is not the terminal)
- `entrypoint`: change the image's default entrypoint - very useful for debugging
- `ci-image`: image name
- `fh-python`: command line argument passed to the entrypoint, if arguments are ambiguous, preceed them
    with `--`. For instance: `docker run my image -d -- --entrypoint-arg-1 hello`

