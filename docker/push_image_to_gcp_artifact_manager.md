# Push image to GCP
## Build
First build your image as usual:
``` sh
docker build -t foo .
```

## Login
Then login to GCP with docker (see the related note).

## Tag
Then tag your image with the whole path
to the docker registry of your choice.
The default is dockerhub if there isn't any
path prepended to the image name.

Let us create two tagged image, with each two
different version tags:
``` sh
docker tag epdl location/project_name/repository/foo:latest
docker tag epdl location/project_name/repository/foo:0.1.0
```

Anything before `foo` (the local image name) refers to the repository
name (`docker.io`). On GCP it is made up of three components:
- `location`: the region where the repository is stored + `-docker.pkg.dev`
    ex: europe-west9
- `project-name`: name of the project holding the repository
    ex: `my-backend-project`
- `repository` - the name of the docker repository
    ex: `fh-docker`

Let us call this `$repository` for the rest of the documentaion.

## Push
``` sh
docker push -a $repository/epdl
```
- `-a`: means to push all tags for the image in one row

