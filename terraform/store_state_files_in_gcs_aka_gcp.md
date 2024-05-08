# Store state files in GCS (on GCP)

Here is the code to add to your main.tf file:
```
terraform {
  backend "gcs" {
    bucket  = "<bucket name>"
    prefix  = "<path to folder>"
  }
}
```

Note - before running terraform make sur you are authenticated
on GCP.

