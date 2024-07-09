# Authenticate poetry to GCP
*IMPORTANT* - This note is only for pulling
private dependencies from GCP. For Publishing,
please refer to `publish_to_gcp` instead.

``` sh
gcloud auth activate-service-account --key-file=path_to_key
poetry config http-basic.fh-python oauth2accesstoken "$(gcloud auth print-access-token)" 
```

`fh-python` is a private repository, replace by your own.

