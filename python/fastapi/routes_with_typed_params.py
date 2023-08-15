"""
This module shows how to provide typed
parameters to an endpoint so that automatic
validation can be carried out by pydantic. 

Check notes about path values. They are
interesting complements to this one.
"""

from uuid import UUID

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "root"}


# Paths (aka routes) are evaluated in order
# So the /me part of /users must be defined
# before /user_id otherwise the latter will
# be called and result in an error because
# 'me' is not a valid uuid
@app.get("/users/me")
def users():
    print("This is me")
    return {"msg": "this is me"}


# Takes a path parameter (required) bearing the name
# user_id of type uuid.UUID
@app.get("/users/{user_id}")
def users(user_id: UUID):
    print(f"user_id == {user_id}")
    return {"user_id": user_id}
