# Domain Name Resolution
`go get` opens `/etc/resolv.conf` to get the default gateway with
a DNS server running (connecting on port 53) to resolved domain
names.

If no domain name resolution serveris defined in `resolv.conf`
then it defaults to querying `127.0.0.1:53` generally resulting 
in a connection refused error because no DNS server listens to 
port 53 on localhost.

To solve this edit resolv.conf and set your local DNS server as domain name
(you can get this running `netstat -rn`).

Here is a simple `/etc/resolv.conf`:
```
nameserver 192.168.1.1
```

