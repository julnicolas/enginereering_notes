# Resolved.service
Service looking up dns servers in use.
It works in conjunction with network managers, especially with 
`systemd-networkd`.

It writes this list in `/run/systemd/resolve/resolv.conf`.
This file is suitable to be softlinked as resolv.conf.

Command to do so:
``` sh
cd /etc
ln -s /run/systemd/resolve/resolv.conf
```

Note - the list is maintained in an internal cache, this cache may have to be cleared
so that resolv.conf can be updated (may be necessary on laptops).
