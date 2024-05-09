# Connect to network

This command shows available networks
``` sh
sudo iwctl
station <interface> scan on
```

Select one of available networks then:
``` sh
station <interface> connect <ssid>
```

