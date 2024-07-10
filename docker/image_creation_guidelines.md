# Image creation guidelines
This note gives guidelines to make efficient images.

## Efficient images in storage size
- Layers are file-system snapshots (maybe not only, refine definition later),
    so to save space, limit layers. Statements such as RUN, COPY, ADD, create
    big layers in size at each call so group calls in `RUN` and use globs in
    `ADD` and `COPY`.
- When installing dependencies, remove the caches after installation
- When installing build dependencies, remove them after build is completed
- If built item is just a binary or a few identifiable binaries, build them
    in a separate stage (using `multi-stage` builds), then copy the output to
    your main image.
- Accessory build stage layers are not part of the main image if the main image
    do not derivate from the accessory stage. It means that multi-stage builds
    can be used extensively to save space.
- `COPY` and `ADD` can be used with `--chown` so that an additional `RUN` layer
    can be avoided
- fill your `.dockerignore` with any build artifact files or sensitive files
    (__pycache__, ...)

### Quality Assessment tools
Two good tools to monitor layers:
- `docker image inspect $IMAGE`
- `dive $IMAGE`

## Security guidelines
- Run the resulting image in non-root user
- If some build, generation process must be done as root user and the output is
    a few identifiable set of files, do this root-stage in an accessory build stage,
    then copy it over to your main image using right `user id`
- As always, think about what unix permissions should be granted to files
- if security is of utter importance over debugging, `FROM scratch` can be used,
    so that a terminal is not even present in the resulting image.

