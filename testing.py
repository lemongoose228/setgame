import json
import requests

ur = "http://192.168.0.15:5000"
uri = ur + "/user/register"
param = {"nickname": "Lem-ababa", "password": "8642"}

response = requests.post(uri, json=param)
if (response.status_code == 200):
    jsn = json.loads(response.text)
    print(jsn)
else:
    print("Ошибка")