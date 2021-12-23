"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
import hashlib


cache = {
    'url_1': '186a1eea0f1da06eeb4c00f468d79ab8c5041fb51e01a48178b9e2e17e73e1a9'
             'f9fde7717ae9c43f52484028e61c10de50c621de27e227b4f8e56b5b886e5571',
    'url_2': 'ffe53196b164f5f4578840c7bd9baeda04d12c7650f2f2d8c99126f8eac5ae0d'
             '1663d728db7cf2d2ecaa30a37a528a7751cfca62abdf3031791093efa1c5466b'
}


def caching(url):
    if url in cache:
        print(f'{url} уже в кэше')
    else:
        salt = uuid4().hex
        cache[url] = hashlib.sha512(url.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        print(cache[url])


caching('url_1')
caching('url_3')
print(cache)
