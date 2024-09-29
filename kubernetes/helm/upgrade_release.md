# Upgrade release
Upgrade the release with to the chart versions
represented by `$chart` using the values from
`values.yml`.

This command can also be used to update the values
used for a release.

``` sh
helm upgrade -f values.yml $release_name $chart
```

