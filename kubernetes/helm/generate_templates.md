# Generate helm templates

Generates the kubernetes manifests into `output dir` using
`values.yml`.

``` sh
helm template -f $values.yml --output-dir $output ./chart
```

