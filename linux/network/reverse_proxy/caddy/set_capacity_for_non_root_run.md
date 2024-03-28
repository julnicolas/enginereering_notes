# Set capacity

Allows to run caddy as non-root user:
``` sh
sudo setcap cap_net_bind_service=+ep $(which caddy)
```

