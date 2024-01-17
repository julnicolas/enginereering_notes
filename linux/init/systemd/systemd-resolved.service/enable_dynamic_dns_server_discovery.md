# Enable Dynamic DNS Server Discovery
On laptops, IP pointing to DNS server can vary as gateway IP 
is likely to be different.

``` sh
cd /etc
mv resolv.conf resolv.conf.bu
ln -s /run/systemd/resolve/resolv.conf
```

