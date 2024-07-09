# Add private package to project
To be able to refer to private dependencies the following steps must be carried out.

## Authenticate to GCP with right service key
To do so please read the part on authentication from the `publish_to_gcp.publish_to_gcp`
note.

## Add a new repository as a source
``` sh
poetry source add --priority=supplemental $REPO_NAME $URL
```
`URL` - read the aforementioned note on how to get the repo's URL.

## Add the new dependency to your pyproject
``` sh
poetry add [--group=xxx] --source $REPO_NAME $PACKAGE_NAME
```

