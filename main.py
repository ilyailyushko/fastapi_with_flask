from fastapi import FastAPI
from fastapi import Request
from flask import Flask
from flask import request
from fastapi.middleware.wsgi import WSGIMiddleware

from fast_bitrix24 import Bitrix

# замените на ваш вебхук для доступа к Bitrix24
webhook = "https://your_domain.bitrix24.ru/rest/1/your_code/"
b = Bitrix(webhook)
auth = 'sajefn23e9ndw928EN9-@(#@(SM(JDWE2D3_'


# Инициализация FastApi
app = FastAPI()
# Инициализация Flask
flask_app = Flask(__name__)

# Встройка Flask в FastApi
app.mount('/flsk', WSGIMiddleware(flask_app))

# Секция Flask

@flask_app.route('/ontask/', methods = ['POST'])
def comment_to_entity():
    r = dict(request.form)
    print(r)
    return 'OK'

@app.get("/")
def read_root():
    return {"ghbdtn": "MIR"}
