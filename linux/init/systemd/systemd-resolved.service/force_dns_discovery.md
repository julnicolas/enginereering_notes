# Force DNS Discovery
`resolved.service` restart a local discovery for DNS servers upon
network changes, so to trigger this the network manager service has
to be restarted.

If the network manager is `systemd-networkd.service`:
``` sh
systemctl restart systemd-networkd.service
```

Then check change is effective by comparing `/etc/resolv.conf` and `netstat -rn`.

Note - `/etc/resolv.conf` is a symlink to `/run/systemd/resolve/resolv.conf`.

