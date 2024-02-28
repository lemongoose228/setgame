from flask import Flask
from flask import request
from secrets import token_hex
from set import Game, ErrorProcessing
app = Flask(__name__)

game = Game()
@app.get("/")
def begining():
    return "Popa"

@app.post("/user/register")
def registr():
    data = request.get_json()
    try:
        response = game.registr(data)
        return response

    except ErrorProcessing as error:
        response = {"success": False, "exception": {}}
        response["exception"]["message"] = error.text
        return response

@app.post("/set/room/create")
def createRoom():
    data = request.get_json()
    try:
        response = game.createRoom(data)
        return response

    except ErrorProcessing as error:
        response = {"success": False, "exception": {}}
        response["exception"]["message"] = error.text
        return response


@app.post("/set/room/list")
def roomlist():
    data = request.get_json()
    try:
        response = game.roomlist(data)
        return response

    except ErrorProcessing as error:
        response = {"success": False, "exception": {}}
        response["exception"]["message"] = error.text
        return response

@app.post("/user/login")
def login():
    data = request.get_json()
    try:
        response = game.login(data)
        return response

    except ErrorProcessing as error:
        response = {"success": False, "exception": {}}
        response["exception"]["message"] = error.text
        return response

@app.post("/set/room/enter")
def enterRoom():
    data = request.get_json()
    try:
        response = game.enterRoom(data)
        return response

    except ErrorProcessing as error:
        response = {"success": False, "exception": {}}
        response["exception"]["message"] = error.text
        return response

app.run(host="0.0.0.0")
