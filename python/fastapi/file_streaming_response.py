""" This shows how to stream a file download
using fastapi. """

from os.path import realpath

from fastapi import FastAPI
from fastapi.responses import FileResponse

file_path = f"{realpath('.')}/hello"
app = FastAPI()


@app.get("/")
async def file():
    return FileResponse(file_path)
