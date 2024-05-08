# Files to store in VCS
Terraform configuration files and the lock file
called `.terraform.lock.hcl`. That's it.

## Reason from terraform's documentation
When terraform init is working on installing all of the providers needed 
for a configuration, Terraform considers both the version constraints in the 
configuration and the version selections recorded in the lock file.

If a particular provider has no existing recorded selection, Terraform will 
select the newest available version that matches the given version constraint, 
and then update the lock file to include that selection.

If a particular provider already has a selection recorded in the lock 
file, Terraform will always re-select that version for installation, 
even if a newer version has become available. You can 
override that behavior by adding the -upgrade option when you run 
terraform init, in which case Terraform will disregard the existing selections 
and once again select the newest available version matching the version constraint.

