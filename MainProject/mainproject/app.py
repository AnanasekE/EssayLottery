from flask import Flask, Response, request

app = Flask(__name__)


@app.post('/users')
def add_user():
    print(request.json)
    return Response(status=501)
