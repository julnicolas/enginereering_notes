# GOPROXY

GOPROXY is a mandatory environment variable
(from go 1.11 if recall well) to fetch go modules.

Its value is comma-separated-list of URLs to proxies
that may contain queried packages. If looked up package
is not found then the next URL is HTTP-get-requested until
either the package is found or the list is exausted.

The special value `direct` tells using software to go fetch
the modules by querying its name with HTTP without modification.
This usually work as module names generally contain a FQDN as well
as a path their location.

Then, `GOPROXY` is used by `go get`, `go install` amongst others.

Finally, `golang 1.13` GOPROXY is set by default to:
``` sh
GOPROXY=proxy.golang.org,direct
```

Which is a sane default for any open-source project.

Then as a final note, `GOPROXY` tags along with `GOSUMDB` which direct
toward a checksum server for go modules. By default it points toward
`GOPROXY` querying an endpoint dedicated to fetch check sums for modules.

