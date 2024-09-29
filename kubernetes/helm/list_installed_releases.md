# List installed releases

First of all, a release is a set of deployed
kubernetes resources identified by an `application version`.
These resources are defined in a helm chart (identified by a chart
version) which after templating generates kubernetes manifests.

To list all installed releases:
``` sh
helm list
```

