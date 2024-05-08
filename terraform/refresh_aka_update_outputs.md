# Refresh output variables
Run this command so that your output variables
can be updated without having to resort to a full
`apply`.

Note - it is possible to do a plan first to check
operations to be executed.

## Plan
``` sh
terraform plan -refresh-only
```

## Apply refresh
``` sh
terraform refresh
```

