""" Show how to return a specific http error code.
run with:
``` sh
uvicorn return_error_code:app [--reload]
```
"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return HTTPException(status_code=409, detail="Retry later")
