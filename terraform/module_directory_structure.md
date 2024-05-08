# Module Directory Structure
Here is how a terraform module looks like:
```
├── README.md
├── main.tf           # declare resources
├── variables.tf      # variables to configure resource
├── outputs.tf        # exposed output information
├── ...
├── modules/
│   ├── nestedA/
│   │   ├── README.md
│   │   ├── variables.tf
│   │   ├── main.tf
│   │   ├── outputs.tf
│   ├── nestedB/
│   ├── .../
├── examples/
│   ├── exampleA/
│   │   ├── main.tf
│   ├── exampleB/
│   ├── .../
```

To deploy an infrastructure with terraform, the `terraform apply` command is
used.

