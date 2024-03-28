# Simple service example

First create the unit file:
``` sh
touch /etc/systemd/system/echo.service
```

Here is a sample content:
```ini
[Unit]
Description=Echo service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=ubuntu
# file containing environment variables
# the optional '-' means that no error
# will be triggered if the file is not present
#EnvironmentFile=-/etc/sysconfig/httpd
ExecStart=/home/foo/myscript.sh"

[Install]
WantedBy=multi-user.target
```

Enable the service:
``` sh
systemctl enable echo.service
systemctl start echo.service
systemctl status echo.service
```

Using the following can also be useful to check logs:
``` sh
journalctl --unit echo.service
```

