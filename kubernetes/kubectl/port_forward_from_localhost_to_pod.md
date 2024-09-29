# Port forward from host to localhost
``` sh
kubectl port-forward mypod 8443:https 6000
```
In this example, local traffic to port 8443 is redirected to `mypod`
on port 443 and local traffic from port 6000 is redirected to pod's
port 6000.

Options
--------
- `--pod-running-timeout=1m0s`: waits up to a minute for the pod to be running.
- `--address=localhost,ip1,ip2`: what addresses to listen to, to redirect traffic
from.

