"""""
Чтобы передавать данные между функциями, модулями или разными системами используются
форматы данных. Одним из самых популярных форматов является JSON.
Напишите декоратор to_json, который можно применить к различным функциям,
чтобы преобразовывать их возвращаемое значение в JSON-формат.
Не забудьте про сохранение корректного имени декорируемой функции.
"""

#decorator dlya jason
import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        mydump=json.dumps(result)
        return mydump
    return wrapper

@to_json
def get_data():
    return {
    'data': 42
    }

print(get_data())