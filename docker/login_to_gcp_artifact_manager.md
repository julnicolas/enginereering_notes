# Login to GCP's artifact manager

``` sh
cat artifact.json | sudo docker login -u _json_key --password-stdin $LOCATION
```

- `artifact.json`: is a service account key with appropriate artifact permissions
- `LOCATION`: url path to GCP's docker repository

