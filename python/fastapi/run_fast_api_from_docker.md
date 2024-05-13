# Run a FastAPI app
``` sh
uvicorn --host 0.0.0.0 main:app [--reload]
```
Where main is `main.py` which instantiates
`app = FastAPI()`.

Setting host to `0.0.0.0` rather than `127.0.0.1`
is important because uvicorn will refuses forwarded
packets comming from `0.0.0.0` with a `recv connection
reset` error.

Forwarding rules must be changed from withing
the container or, uvicorn controls the incoming IP.
It would be great to know precisely.

