
import os
import time
from os import getcwd

#print(getcwd())
#os.path.abspath('path')

#keys_dict = dict(os.environ)
#print(keys_dict.keys())

import requests
#import json

time_beg = time.perf_counter()
url = 'http://muslimsalat.com/daily.jsons'
data = {
    'username': 'username', 
    'password': 'password'
    }
get = requests.get(url)
post = requests.post(url + '/login', data=data)

if get.status_code == 200:
    print('Наш GET успешно достиг example.com')
    print('Ответ в тексте будет представлять собой: ')
    print(get.json())
else:
    print('Что-то пошло не так')

if post.status_code == 200:
    print('Авторизация прошла успешно')
else:
    print('Что-то пошло не так, код ошибки -', post.status_code)


#import time
#while True:
#    print("It's okay")
#    time.sleep(1)


print(time.perf_counter() - time_beg)

import logging
logging.basicConfig(filename='log_file.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning! Something happened!')
logging.error('Error!')
logging.critical('Critical error!!!')

# Эксперимент:
#1. Принимает в качестве параметров требуемое количество записей и задержку (соответственно, 
# он должен запускаться с терминала с указанием необходимых параметров).

# python './PY 10_1.py' 1 2 3
x = sys.argv[1:]
y = int(x[0]) # Определяет задержку

if len(x) == 3: 
    time.sleep(y)
    print(f"Количество записей = 3. задержка = {y} сек.")
else:
    time.sleep(y)
    print (f"Введите кол-во записей = 3. задержка = {y} сек.")


time.sleep = x[1]