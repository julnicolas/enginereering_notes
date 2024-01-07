# GOSUMDB
Source `go.dev/doc/go1.13`
Exists since `go 1.13`.

The new `GOSUMDB` environment variable identifies the name, and 
optionally the public key and server URL, of the 
database to consult for checksums of modules that are not 
yet listed in the main module’s go.sum file. If GOSUMDB does 
not include an explicit URL, the URL is chosen by probing the GOPROXY 
URLs for an endpoint indicating support for the checksum database,
falling back to a direct connection to the named database if it 
is not supported by any proxy. If GOSUMDB is set to off, the checksum 
database is not consulted and only the existing checksums in the 
go.sum file are verified.

For any reason if the checksum cannot be reached by `go get` here is
the way to disable it:
``` sh
export GOSUMDB=off
```

## Value examples
``` sh
export GOSUMDB="sum.golang.org"
export GOSUMDB="sum.golang.org+<publickey>"
export GOSUMDB="sum.golang.org+<publickey> https://sum.golang.org"
```

