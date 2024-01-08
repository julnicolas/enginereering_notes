# resolv.conf config file
`resolv.conf` is used as a reference file to
get the IP address of the name server to query
to resolve domain names into IP addresses.

Some tools such as `dig`, `host`, `go get` open
this file to know what IP to query to. If it is empty
then they default to `127.0.0.1` generally resulting in
connection error as there is rarely a local DNS server
listnening on default DNS port `53`.

Some other tools will query `0.0.0.0:53` instead, which will
work as DHCP clients edit the kernel's routing table to redirect
`0.0.0.0` to the LAN's gateway.
-> Check this is effectively a consequence of DHCP configuration,
but it is very likely.

## Simple configuration to avoid the connection error
- run `netstat -rn` to get the routing table (
netstat is in net-tools package).
- look at the gateway IP address at destination `0.0.0.0`
let's call it `my_address`
- then edit `/etc/resolv.conf` as follows:
```
nameserver my_address
```

