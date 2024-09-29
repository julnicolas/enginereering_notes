# Inspect configurable values
The command output a list of values with their
documentation. Returned values can be overriden
by users in their value files.

Note - a local path to a helm chart or a url to a
chart can be given to helm.

``` sh
helm inspect values $chart_uri
```
`uri` above is either a local path or a url.

