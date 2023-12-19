# Build args VS env vars
Build args are used at build stage only. They are used to parameterise the build
stage. Example usage:
- define image version or tags
- fillout environment variables

Environment variables are defined at `docker run` stage. They define `runtime` parameters.

