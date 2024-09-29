# Helm components
`Helm` is made up of two components:
- `helm`: a CLI tool used to interact with helm charts
- `tiler`: a kubernetes controler used to apply helm charts
	changes to kubernetes resources. It also keeps track of
	charts versions within the cluster.

## Installation process
``` sh
helm init --history-max 200
```

