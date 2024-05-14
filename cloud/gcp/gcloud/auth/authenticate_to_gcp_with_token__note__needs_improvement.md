# Authenticate using a token

``` sh
export GOOGLE_ACCESS_TOKEN=ya29.a0AfH6SMC78...
```

If GOOGLE_ACCESS_TOKEN is set all other authentication mechanisms are disabled. The 
access token must have at least the `https://www.googleapis.com/auth/devstorage.read_write`
scope. Keep in mind that access tokens are short-lived (usually one hour), 
so they are not suitable if creating a backup takes longer than that, for instance.

