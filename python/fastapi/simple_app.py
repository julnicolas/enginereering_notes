from fastapi import FastAPI

# To run the app from a terminal:
# uvicorn main:app [--reload]
# reload is used to reload a modified file, good for dev
app = FastAPI()

# GET http://localhost:8000/
@app.get("/")
async def root():
    # Returns a response body encoded in json
    # headers["Content-Type"] is set to "application/json"
    return { "msg": "hello" }

# GET http://localhost:8000/foo
@app.get("/foo")
async def foo():
    # It also returns a json datastructure
    return [1, 2, 3]
