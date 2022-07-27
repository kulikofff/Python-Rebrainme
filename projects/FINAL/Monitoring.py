import os
import psutil
import time
import json
import logging
from os import environ, getlogin
from psutil import virtual_memory, getloadavg
import requests as requests
import jsonpickle

#Задержка
t = 60

#Установка параметров логирования

logging.basicConfig(filename='log_file.log', format='%(asctime)s %(levelname)s %(message)s', datefmt='%b %d %H:%M:%S', level=logging.INFO)
logging.basicConfig(filename='log_file.log', format='%(asctime)s %(levelname)s %(message)s', datefmt='%b %d %H:%M:%S', level=logging.ERROR)

def datainfo():  
    class HOSTINFO:
        sys_name: str = psutil.users()[0].name
        host_name: str = psutil.users()[0].host if psutil.users()[0].host else 'localhostAVK'
        def show_sysname(self):
            return self.sys_name
        def show_hostname(self):
            return self.host_name
        
    class NETWORK:
        @staticmethod
        def get_stat(status: bool):
            return "Up" if status else "Down"

        def show_stat(self):
            net_stat = psutil.net_if_stats()
            net = []
            for key, value in net_stat.items():
                net.append({'interface': self.get_stat(value.isup)})
            out = net[0]
            return out

        def show_mtu(self):
            net_stat = psutil.net_if_stats()
            net = []
            for key, value in net_stat.items():
                net.append({'mtu': value.mtu})
            out = net[0]
            return out

    class DISK:
        partitions = psutil.disk_partitions()

        def show_disk_name(self):
            disk = []
            for partition in self.partitions:
                    disk.append({'disk': partition.device})
            out = disk[0]
            return out
        
        def show_mount_point(self):
            mountpoint = []
            for partition in self.partitions:
                    mountpoint.append({'mountpoint': partition.mountpoint})
            out = mountpoint[0]
            return out

        def show_file_system_type(self):
            file_system_type = []
            for partition in self.partitions:
                    file_system_type.append({'file_system_type': partition.fstype})
            out = file_system_type[0]
            return out

        def show_total(self):
            disk =  self.show_mount_point()
            for value in disk.values():
                disk_usage = psutil.disk_usage(value)
                total = {'total': disk_usage.total}
                return total

        def show_used(self):
            disk =  self.show_mount_point()
            for value in disk.values():
                disk_usage = psutil.disk_usage(value)
                used = {'used': disk_usage.used}
                return used 

    class MEMORY:
        memory: int = virtual_memory()
        show_total_mem: int = memory.total
        show_used_mem: int = memory.used
        show_per_mem: float = memory.percent

        def show_total(self):
            return self.show_total_mem
        def show_used(self):
            return self.show_used_mem
        def show_per(self):
            return self.show_per_mem      


    class CPU:
        cpu_cores: int = psutil.cpu_count()
        cpu_physical_cores: int = psutil.cpu_count(logical=False)
        cpu_frequency: int = psutil.cpu_freq()

        def show_cpu(self):
            return self.cpu_cores
        def show_cores(self):
            return self.cpu_physical_cores
        def show_freq(self):
            a =  self.cpu_frequency[0]
            b =  self.cpu_frequency[1]
            c =  self.cpu_frequency[2]
            return a, b, c


    class LOADAVG:
        load_average = psutil.getloadavg()
        one_min: float = load_average[0]
        five_min: float = load_average[1]
        fifteen_min: float = load_average[2]

        def info_load(self):
            return [{'1 min': self.one_min,
                    '5 min': self.five_min,
                    '15 min': self.fifteen_min},
                    ]
  
    info_host = HOSTINFO()
    info_net = NETWORK()
    info_disk = DISK() 
    info_mem = MEMORY()
    info_cpu = CPU()
    info_load = LOADAVG() 
    host_dict = {'sysname': info_host.show_sysname(), 'hostname': info_host.show_hostname()}
    net_dict = [{**info_net.show_stat(), **info_net.show_mtu()}]
    disk_dict = [{**info_disk.show_disk_name(), **info_disk.show_mount_point(), **info_disk.show_file_system_type(), **info_disk.show_total(), **info_disk.show_used()}]
    mem_dict = {'memory_total': info_mem.show_total(), 'memory_used': info_mem.show_used(), 'memory_percent': info_mem.show_per()} 
    cpu_dict = {'cpu_cores': info_cpu.show_cpu(), 'cpu_physical_cores': info_cpu.show_cores(), 'cpu_freqency': {info_cpu.show_freq()}}
    dict ={'host_information' : host_dict, 'network': net_dict, 'disk': disk_dict, 'memory': mem_dict, 'cpu': cpu_dict, 'load_average': info_load.info_load()}

    return dict

def fordjango_descr():
    #"DESC" в windows нет.
    try:
        description = (os.environ["DESC"])
    except(KeyError):
        description = input(f"Вероятно, у Вас установлено Windows, введите описание вручную: ")
    return description

def fordjango_name():
#"hostname" в windows нет.
    try:
        name = (os.environ["hostname"])
    except(KeyError):
        name = input(f"Вероятно, у Вас установлено Windows, введите имя сервера вручную: ")
    return name

description = fordjango_descr()
name = fordjango_name()

def django(dataresult):
    ipaddress = requests.get('https://ifconfig.me/ip').text
    status = True

# Устранение ошибки "TypeError: Object of type set is not JSON serializable"
    data_active = jsonpickle.encode(dataresult)
# Для вывода ошибки при отправке данных в Django
#    data_active = (dataresult)     


    data = {'name': name,
            'ip_address': ipaddress,
            'description': description,            
            'server_is_active': status,
            'data_active': data_active}
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.post('http://127.0.0.1:8000/api/servers/add', data=json.dumps(data), headers=headers)
        if response.status_code == 201:
        # Успешная регистрация сервера:
                
                logging.info('Успешная регистрация сервера и отправка данных')
                print('Успешная регистрация сервера и отправка данных:')
                return data
        else:
        # Неуспешная регистрация сервера:
                logging.error('Отказ отправки данных')
                print('Отказ отправки данных')
    except(TypeError):
        logging.error('Отказ регистрации сервера')
        print('Отказ регистрации сервера')

    return


if __name__ == '__main__':
    while True:
#Старт программы:
        logging.info('Старт программы')
        dataresult = datainfo()
        print(f'Данные для отправки: {dataresult}')
        logging.info(f'Полученный в результате работы массив данных о системе: {dataresult}')
#Полученный массив данных:
        logging.info('Получен массив данных о системе')
#Обработка ошибки недоступности сервера:
        try:
            print(django(dataresult))
        except(requests.exceptions.RequestException):
            logging.error('Отказ регистрации сервера')
            print(f'Запустите сервер Django и подождите не более {t} секунд')

        time.sleep(t)


