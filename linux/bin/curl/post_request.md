# Post Request
``` sh
curl -X POST -H "Content-Type: $content" \
-d "$DATA" \
-w '%{http_code}' \
'url'
```
- `-H` is a http header
    Example `$content`:
    - `application/json`
    - `multipart/form-data`
- `-d` is the request's body
- `-w` stands for "write out" - write the status code

