#4. Создайте файл-модуль. Используя модуль os и функцию getlogin, а также модуль psutil и функцию virtual_memory, создайте словарь со следующими полями: 'user_name', 'memory_total', 'memory_used' и 'memory_percent'
#  и заполните эти поля данными, полученными из функций.

from os import getlogin
from psutil import virtual_memory

user_name: str = getlogin()
mem_info: int = virtual_memory()

def mem_used() -> dict:
        dict1 = {'user_name': user_name, 'memory_total': mem_info.total, 'memory_used': mem_info.used, 'memory_percent': mem_info.percent}
        return dict1
