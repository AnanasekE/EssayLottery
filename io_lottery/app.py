import json

from flask import Flask, Response, request

from io_lottery.controllers import AddUserController, AddUserRequest

app = Flask(__name__)


# @app.post("/users")
# def add_user() -> Response:
#     controller = AddUserController()
#     controller.add(request=AddUserRequest(json=request.json))
#     return request.json


@app.get("/users")
def get_user() -> Response:
    return Response(status=501)


@app.post("/users")
def add_user() -> Response:
    return Response(status=201)


@app.put("/users/<int:user_id>")
def update_user(user_id: int) -> Response:
    return Response(status=200)


@app.patch("/users/<int:user_id>")
def patch_user(user_id: int) -> Response:
    return Response(status=200)


@app.delete("/users/<int:user_id>")
def delete_user(user_id: int) -> Response:
    return Response(status=204)
