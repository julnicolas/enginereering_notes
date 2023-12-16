# Publish a python package to GCP
## Setup GCP
First, create an `artifact registry` on GCP. Then create
a service account with a key with sufficient priviledges to
read and write on the repository.

## Get repository's URL from a gcloud console
Type the following command on a GCP console to get your repo's URL.
``` sh
gcloud artifacts print-settings python \
    --project=$PROJECT_ID \
    --repository=$REPO_NAME \
    --location=$REGION
```

## Install Gcloud
Gcloud must be installed so that auth can be carried out. Follow google's instructions
for this.

## Download the service key
Download the service key made with the service account at step 1.

## Authenticate with the service key
``` sh
gcloud auth activate-service-account --key-file="full_path_to_service_key"
```

## Add the private repository to poetry with connection credentials
To add the repository:
``` sh
poetry config repositories.<REPO_NAME> 'https://<ZONE>-python.pkg.dev/<PROJECT_ID>/<REPO_NAME>'
```
This URL format is subject to changes.
The stable way to get the URL is by the `get repository's URL` step. Important - no `/simple` here. `/simple`
is one of the `pypy protocol` for downloading packages. Here this is for upload!

``` sh
poetry config http-basic.fh-python oauth2accesstoken "$(gcloud auth print-access-token)"
```

## Build the package
``` sh
poetry build
```

## Publish it to the private repo
``` sh
poetry publish --repository $REPO_NAME
```

