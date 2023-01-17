from flask import Flask, Response, request

app = Flask(__name__)


@app.post("/users")
def add_user() -> Response:
    return request.json


@app.get("/users")
def get_user() -> Response:
    return Response(status=501)
