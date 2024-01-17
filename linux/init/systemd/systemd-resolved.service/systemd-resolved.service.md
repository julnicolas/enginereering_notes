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

Note that the list may need to be refreshed if laptop or mobile
changed its connection access point. Read relevent note to learn
how to do so.

