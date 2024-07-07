# Remove image
``` sh
docker image rm $img_hash
```

``` sh
docker image rm $(docker image ls -qs)
```

