# PAT and HTTPS support
Download caddy from github (single bin).

Then run the following:
``` sh
caddy reverse-proxy --from domain[:port] --to :port
```

If domain is ommited, localhost name and self-signed
certificates will be used.

If domain corresponds to a domain you own, caddy generates
a letsencrypt certificate automatically.

If no ports are given in the `--from` flag then it is assumed
both port `80` and `443` must be redirected. Make sure to allow
traffic to both ports.

