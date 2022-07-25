import os
import psutil
import time
from os import environ, getlogin
from psutil import virtual_memory, getloadavg

#Задержка
t = 1

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
        pass

    class DISK:
        pass

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
        pass

  
    info_host = HOSTINFO()
    info_mem = MEMORY()
    info_cpu = CPU() 
    host_dict = {'sysname': info_host.show_sysname(), 'hostname': info_host.show_hostname()}
    mem_dict = {'memory_total': info_mem.show_total(), 'memory_used': info_mem.show_used(), 'memory_percent': info_mem.show_per()} 
    cpu_dict = {'cpu_cores': info_cpu.show_cpu(), 'cpu_physical_cores': info_cpu.show_cores(), 'cpu_freqency': {info_cpu.show_freq()}}
    dict ={'host_information' : host_dict, 'memory': mem_dict, 'cpu': cpu_dict}
    return dict 


if __name__ == '__main__':
    while True:
        print(datainfo())
        time.sleep(t)





