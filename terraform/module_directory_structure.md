# Module Directory Structure
Here is how a terraform module looks like:
```
README.md
main.tf       // contains the infrastructure description
variables.tf  //contains variable definitions
output.tf     // contains variables computed from infrastructure application*
```

To deploy an infrastructure with terraform, the `terraform apply` command is
used.

