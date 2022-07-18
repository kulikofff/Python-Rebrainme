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

info_pc_env = PC_memory('AVK_PC', name, memory.total, memory.used)

print(info_pc_env.show_used_percent())
print(info_pc_env.is_enough_memory())