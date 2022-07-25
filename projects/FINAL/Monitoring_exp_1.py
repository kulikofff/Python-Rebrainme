import os
import psutil
import time
from os import environ, getlogin
from psutil import virtual_memory, getloadavg

#Задержка
y1 = 60

class HOSTINFO:
    pass
class NETWORK:
    pass
class DISK:
    pass
class MEMORY:
    pass

class CPU:
    cpu_cores: int = psutil.cpu_count()
    cpu_physical_cores: int = psutil.cpu_count(logical=False)
    cpu_frequency: int = psutil.cpu_freq()

    def show_cpu(self):
        return self.cpu_cores
    def show_cores(self):
        return self.cpu_physical_cores
    def show_freq(self):
        return self.cpu_frequency

class LOADAVG:
    pass

info_cpu = CPU()    

cpu_dict = {'cpu_cores': info_cpu.show_cpu(), 'cpu_physical_cores': info_cpu.show_cores(), 'cpu_freqency': {info_cpu.show_freq()}}
dict ={'cpu': cpu_dict}

while True: 
    print(dict)
    time.sleep(y1)