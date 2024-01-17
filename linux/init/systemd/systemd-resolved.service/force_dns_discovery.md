# Force DNS Server Discovery

Flush cache:
``` sh
kill -SIGUSR2 $resolved_pid
```

Restart service:
``` sh
systemctl restart systemd-resolved.service
```

