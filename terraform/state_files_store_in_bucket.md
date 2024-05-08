# Why state files must be stored in buckets and not in a VCS?
- They contain sensitive data (passwords, keys)
- They can be accessed concurrently from different actors,
    in those case locks can only be effective if the location
    is unique and shared.

NOTE - `terraform apply -lock=true` sets a lock on state file.

