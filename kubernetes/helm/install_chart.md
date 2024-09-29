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

Note
----
- A chart repository (as we’ve seen above)
- A local chart archive (helm install foo-0.1.1.tgz)
- An unpacked chart directory (helm install path/to/foo)
- A full URL (helm install https://example.com/charts/foo-1.2.3.tgz)

