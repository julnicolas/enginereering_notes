# Define output variables

The code below is to be written to `outputs.tf`.
It takes an ip address from a hetzner server as an example.

```
output "ip" {
  # resource.resource_name.field
  value = hcloud_server.epdl-backend.ipv4_address
}
```

