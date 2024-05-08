# Authenticate to GCP

Download or generate a `service-account` key then run the following command:
``` sh
gcloud auth activate-service-account --key-file="full_path_to_service_key"
```

Some applications need the following environment variable to work well 
(on top of the above):
```
export GOOGLE_APPLICATION_CREDENTIALS="$key_path"
```

