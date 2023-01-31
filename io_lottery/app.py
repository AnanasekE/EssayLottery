import json

from flask import Flask, Response, request

from io_lottery.controllers import AddUserController, AddUserRequest

app = Flask(__name__)


@app.post("/users")
def add_user() -> Response:
    controller = AddUserController()
    controller.add(request=AddUserRequest(json=request.json))
    return request.json


@app.get("/users")
def get_user() -> Response:
    return Response(status=501)
