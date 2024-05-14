# Tag image
Tagging an image can mean several things:
- give an image a local alias
- prepare it for a push by prepending a path
    to a docker repository
- appending a version/distribution tag such as `latest`
    note: the version tag is noted after colons, it can
    be alphanumeric and include dashes and dots. 

``` sh
docker tag <local image> <new name>[:<version-tag.something...>]
```

