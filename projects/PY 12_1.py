import os
import psutil
from os import environ, getlogin
from psutil import virtual_memory, getloadavg

class PC_memory:
    def __init__(self, pc_id: str, user_name: str, memory_total: int, memory_used: int, memory_percent: float = None):
        self.pc_id = pc_id
        self.user_name = user_name
        self.memory_total = memory_total
        self.memory_used = memory_used
        self.memory_percent = memory_percent

        if memory_percent:
            self.memory_percent = memory_percent
        else:
            self.memory_percent = memory_used*100/memory_total

    def show_used_percent(self):
        print(f'PC with id {self.pc_id} used {self.memory_percent:2.1f} percent of memory')

    def is_enough_memory(self):
        if self.memory_percent < 10:
            return False
        else: 
            return True    
        
name: str = getlogin()
memory: int = virtual_memory()
loadavg = getloadavg()

class PC_advanced(PC_memory):

    def __init__(self, pc_id: str, user_name: str, memory_total: int, memory_used: int, ld_avg_1m: float, ld_avg_15m: float, memory_percent: float = None):
        super().__init__(pc_id, user_name, memory_total, memory_used, memory_percent)
        self.ld_avg_1m = ld_avg_1m
        self.ld_avg_15m = ld_avg_15m

    def is_overloaded(self):
### В windows команда loadavg выдает (0.0, 0.0, 0.0). Таким образом выводится ошибка ZeroDivisionError: float division by zero.
### Поэтому прибавляю "0.001". На Linux проверил - работает без прибавления единицы. Результат loadavg -> (0.52, 0.58, 0.59)
        if (self.ld_avg_1m+0.001)/(self.ld_avg_15m+0.001) >= 3:
            return True
        else: 
            return False

    def __call__(self, string: str = 'memory', *args, **kwargs):
        if string == 'memory':
            return self.is_enough_memory()
        elif string == 'load':
            return self.is_overloaded()
        else:
            return None



info_pc_env = PC_advanced('AVK_PC', name, memory.total, memory.used, ld_avg_1m=loadavg[0], ld_avg_15m=loadavg[2])

print(info_pc_env.is_overloaded())
print(info_pc_env())


