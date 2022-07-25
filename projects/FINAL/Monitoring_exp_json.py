import os
import psutil
import time
import json
from os import environ, getlogin
from psutil import virtual_memory, getloadavg
import requests as requests
import jsonpickle

#Задержка
t = 60

loadavg = getloadavg()

def datainfo():  
    class HOSTINFO:
        sys_name: str = psutil.users()[0].name
        host_name: str = psutil.users()[0].host if psutil.users()[0].host else 'localhostAVK'
        def show_sysname(self):
            return self.sys_name
        def show_hostname(self):
            return self.host_name
        
    class NETWORK:
#        def get_status(status: bool):
#            return "Up" if status else "Down"

        def show_stat(self):
            net_stat = psutil.net_if_stats()
            net = []
            for key, value in net_stat.items():
                net.append({'interface': value.isup})
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
            disk_usage = psutil.disk_usage('C:\\')
            total = {'total': disk_usage.total}
            return total

        def show_used(self):
            disk_usage = psutil.disk_usage('C:\\')
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
    net_dict = [info_net.show_stat(), info_net.show_mtu()]
    disk_dict = [info_disk.show_disk_name(), info_disk.show_mount_point(), info_disk.show_file_system_type(),info_disk.show_total(),info_disk.show_used()]
    mem_dict = {'memory_total': info_mem.show_total(), 'memory_used': info_mem.show_used(), 'memory_percent': info_mem.show_per()} 
    cpu_dict = {'cpu_cores': info_cpu.show_cpu(), 'cpu_physical_cores': info_cpu.show_cores(), 'cpu_freqency': {info_cpu.show_freq()}}
    dict ={'host_information' : host_dict, 'network': net_dict, 'disk': disk_dict, 'memory': mem_dict, 'cpu': cpu_dict, 'load_average': info_load.info_load()}
    
    return dict


def django(dataresult):
    ipaddress = requests.get('https://ifconfig.me/ip').text
#"DESC" в windows нет:(
    description = (os.environ["OS"])
#"hostname" в windows нет:(
    name = (os.environ["COMPUTERNAME"])
    status = True

# Устранение ошибки "TypeError: Object of type set is not JSON serializable"
    data_active = jsonpickle.encode(dataresult)

    data = {'name': name,
            'ip_address': ipaddress,
            'description': description,            
            'server_is_active': status,
            'data_active': data_active}
    headers = {'Content-type': 'application/json'}

    response = requests.post('http://127.0.0.1:8000/api/servers/add', data=json.dumps(data), headers=headers)

    return data


if __name__ == '__main__':
    while True:
        dataresult = datainfo()
        print(django(dataresult))
        time.sleep(t)





# do UP/Down вместо True/False
# проблема в списке с {}
# поймать ошибку DESC