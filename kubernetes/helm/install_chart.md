# Install chart

To install a chart (creating associated
resources in the cluster) do:

``` sh
# Fetch last changes from helm repositories
# TODO: Check if that operation is always necessary
helm repo update
helm install stable/mysql
```

In this example `mysql` is installed from the stable repository.

