#1. Создайте новый проект, а в нем создайте виртуальное окружение. Задействуйте это окружение.
# python -m venv PY09
# .\PY09\Scripts\activate

#2. С помощью пакетного менеджера установите пакет psutil.
#pip3 install psutil
#(PY09) PS C:\Kulikov\Python\Python-Rebrainme\projects> pip3 list
#Package    Version
#---------- -------
#pip        21.1.1
#psutil     5.9.1
#setuptools 56.0.0

# Вне окружения:
#PS C:\Users\demak> pip3 list
#Package    Version
#---------- -------
#pip        21.1.1 
#setuptools 56.0.0 

#3. Создайте файл с зависимостями с именем requirements.txt
#pip3 freeze > requirements.txt

#5. Создайте основной файл проекта. Импортируйте из него ваш созданный в предыдущем пункте файл и выведите словарь,
#  сформированный в этом файле, на экран.

from module_1 import mem_used
print(mem_used())