# Imperative Object Configuration
Set of commands, taking single Object (aka resource) definition
file to apply command change to the cluster. No adaptative change
is made, just what is described in the file.

Gotcha
------
Files must be updated so that they reflect object state in cluster. Otherwise
further file application will override current change

K8s team recomendation
----------
Use these documentations in dev context.

Further observation from myself
------------------------------
Can be useful to spawn a quick debug helper.

No production management with these tools.

## Command example
``` sh
kubectl create -f nginx.yaml
kubectl delete -f nginx.yaml -f redis.yaml
```

This one is *very dangerous* as it will replace existing resource by the one
in the file. Changes in cluster will be overwritten if file and live resource
differ.
``` sh
kubectl replace -f nginx.yaml
```

