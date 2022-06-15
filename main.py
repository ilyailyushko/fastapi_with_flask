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
def get_task_uf_field():
    """"
    Метод для подписки на создание / изменение задачи
    """
    r = dict(request.form)
    task_id = r['data[FIELDS_AFTER][ID]']
    print('Создана задача, id', task_id)
    requests.post(f'http://194.67.119.72/tasks_task_update_by_uf_field/?task_id={task_id}')

    return 'OK'

@app.get("/")
def read_root():
    return {"ghbdtn": "MIR"}

@app.post('/tasks_task_getFields/')
def tasks_task_getFields():
    '''
    ## Метод для получения полей задачи
    '''
    task_fields = b.call('tasks.task.getFields', raw=True) 
    return task_fields


@app.post('/tasks_task_update_by_uf_field/')
def tasks_task_get_uf_value(task_id):
    """ 
    # Обновление задачи по содержанию кастомного поля
    Метод получает значение пользовательского поля задачи,  если оно заполненно, добавляет в задачу префикс и соответсвующий тег. 
    """
    get_task = b.call('tasks.task.get', {'taskId': task_id, 'select': ['UF_AUTO_395874465748', "TITLE", "DESCRIPTION"]})
    task = get_task['task']
    title = task['title']
    description = task['description']
    uf_field = task['ufAuto395874465748'] 
    print(task)
    if task['ufAuto395874465748']:
        title = f"[{uf_field}] {title}"
        description = f"{description} \n\n #{uf_field}"
        b.call('tasks.task.update', {'taskId': task['id'], 'fields': {"TITLE": title, "DESCRIPTION": description}})
        return task['id'], 'задача обновлена'
    else:
        return 'пользовательское поле задачи не заполненно'
