# Usual Workflow With Terraform
## Initialising
### Create secret file
Before all steps, start by creating a new `terraform.tfvars`
with the following content:

```
token = "<SECRET>"
```
The secret can be found on GCS.

## Authenticate to GCS
Download the appropriate bucket-read-write-service key.
Then run the following command:

``` sh
export GOOGLE_APPLICATION_CREDENTIALS="<path to service key>"
gcloud auth activate-service-account --key-file="terraform.json"
```

## Setting up terraform
The following command instals necessary dependencies
such as required providers.

``` sh 
terraform init
```

## Show Plan's Modifications
Prior to applying the plan to modify
infrastructure. Run the following command to show
the steps of the next apply command:

``` sh
terraform plan
```

## Apply changes
Run the following command to make changes effective:

``` sh
terraform apply
```

## Show Active Resources
``` sh
terraform show
```

To explicitely list only `output` variables:
``` sh
terraform output
```

## Destroy Resources
To destroy all allocated resources:
``` sh
terraform destroy
```

