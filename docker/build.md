# Docker Build
Creates a docker image. Extensive arguments are showned to remember the syntax.

``` sh
sudo docker build -t image_name:image_tag --build-arg ARG1=hello --file containers/f1.dockerfile .
```
- `t`: sets image name and tag
- `build-arg`: this is an argument passed at `build` time used to set up build stage. It can be used
    to populate environment variables
- `file`: path to dockerfile to use to build the image. By default uses the `Dockerfile` in the current
    context.
- context (.): Where to find the dockerfile (by default) and defines root dir of every docker commands

