# Show Status Code
Add `-w %{http_code}` to any request.

``` sh
curl -w '%{http_code}' url
```

