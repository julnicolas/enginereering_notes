# Declarative Object Configuration
Set of commands determining what operation to take on a kubernetes
cluster based on resource definition files in yaml or json.

They can browse directories recursively as well as taking individual
files.

The major difference with the imperative approach is that users do not
get to tell what mutation operation to make to the cluster. These commands
determine them themselves by checking local files against their live object
in the cluster.

Such mutation operation are the following:
- `create`
- `patch`
- `delete`

## Command Examples
Parses all files in config then show expected changes against the cluster:
``` sh
kubectl diff [-R] -f configs/
```

Apply changes to the cluster. Changes are found by browsing all resources
in "configs".
``` sh
kubectl apply [-R] -f configs/
```

Note
----
- `-R` is used to parse directories recursively

