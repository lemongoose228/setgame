from flask import Flask
from flask import request
from secrets import token_hex

class User:
    def __init__(self, id, nickname, password):
        self.id = id
        self.nickname = nickname
        self.password = password
        self.token = token_hex(6)

class Room:
    def __init__(self, id):
        self.id = id
        self.players = []
    def addplayer(self, player):
        self.players.append(player)

class Game:
    users = []
    rooms = []

    def registr(self, data):
        nickname = data["nickname"]
        password = data["password"]
        id = len(self.users)
        for i in self.users:
            if i.nickname == nickname:
                raise ErrorProcessing("Такой пользователь уже существует")

        newuser = User(id, nickname, password)
        self.users.append(newuser)

        response = {}
        response["accessToken"] = newuser.token
        response["nickname"] = newuser.nickname
        return response


    def login(self, data):
        nickname = data["nickname"]
        password = data["password"]
        for i in self.users:
            if i.nickname == nickname:
                if i.password == password:
                    response = {}
                    response["accessToken"] = i.token
                    response["nickname"] = i.nickname
                    return response
                else:
                    raise ErrorProcessing("Неверный пароль")

        raise ErrorProcessing("Пользователь не зарегистрирован")


    def findRoomById(self, gameid):
        for room in self.rooms:
            if room.id == gameid:
                return room

        raise ErrorProcessing("Такой комнаты не существует")

    def findByToken(self, checktoken):
        for user in self.users:
            if user.token == checktoken:
                return user
        raise ErrorProcessing("Такого пользователя нет")


    def roomlist(self, data):
        token = data["accessToken"]
        self.findByToken(token)
        games = []
        response = {}
        for i in self.rooms:
            games.append({"id": i.id})

        response["games"] = games
        return response


    def createRoom(self, data):
        token = data["accessToken"]
        user = self.findByToken(token)
        id = len(self.rooms)
        newroom = Room(id)
        newroom.addplayer(user)
        self.rooms.append(newroom)

        response = {}
        response["success"] = True
        response["exception"] = "null"
        response["gameId"] = newroom.id
        return response


    def enterRoom(self, data):
        token = data["accessToken"]
        gameid = data["gameId"]
        user = self.findByToken(token)
        room = self.findRoomById(gameid)
        room.addplayer(user)

        response = {}
        response["success"] = True
        response["exception"] = "null"
        response["gameId"] = room.id
        return response



class ErrorProcessing(BaseException):
    def __init__(self, text):
        self.text = text


