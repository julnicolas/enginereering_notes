# Variables
They are three types of variables:
- input: typed variable with a description
    and a default. These variables can be
    populated from the CLI or `tfvars` files
    (haven't checked for tvars but seems logical)
- output: populated from `terraform apply`
    results
- locals: name set on a specific value
    (string, int) for commodity
