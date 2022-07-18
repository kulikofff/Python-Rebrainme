'''
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

'''
class Num:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b

a = Num(10, 11)
print(a.sum())

###
class Class_1:
    param_1 = 'Class_1'
    def Output_1(self):
        return self.param_1

class Class_2(Class_1):
    param_2 = 'Class_2'
    def Output_2(self):
        return self.param_2

a = Class_2()
print(a.Output_2(), a.Output_1(), a.param_1)

###
class My_list(list):
    def double_append(self, val):
        self.extend([val, val])
    def clear(self):
        print('unable to clear this list')

my_list_1 = My_list([1, 2])
my_list_1.append(20)
my_list_1.double_append(10)
print(my_list_1)  # [1, 2, 20, 10, 10]
my_list_1.clear() # unable to clear this list
print(my_list_1)

###
class Num:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return self.a + self.b + other

a = Num(10, 11)
print(a + 20)

###


class Num:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a + self.b == other

    def __getitem__(self, item):
        if item == 0:
            return self.a
        elif item == 1:
            return self.b
        else:
            raise IndexError

    def __str__(self):
        return str(self.a) + ' ' + str(self. b)

a = Num(10, 11)
print(a == 21) # True
print(a[0])    # 10
print(a)       # 10 11

###

class Two_attrs:
    def __init__(self, attr_1, attr_2):
        self.attr_1 = attr_1
        self.attr_2 = attr_2

    def sum_attrs(self):
        return self.attr_1 + self.attr_2


class Four_attrs(Two_attrs):
    def __init__(self, attr_1, attr_2, attr_3, attr_4):
        Two_attrs.__init__(self, attr_1, attr_2)
        self.attr_3 = attr_3
        self.attr_4 = attr_4

    def sum_attrs(self):
        return Two_attrs.sum_attrs(self) + self.attr_3 + self.attr_4


a = Two_attrs(10, 20) 
print(a.sum_attrs()) # 30
b = Four_attrs(30, 40, 50, 60) 
print(b.sum_attrs()) # 180

###
class Four_attrs(Two_attrs):
    def __init__(self, attr_1, attr_2, attr_3, attr_4):
        super().__init__(attr_1, attr_2)
        self.attr_3 = attr_3
        self.attr_4 = attr_4

    def sum_attrs(self):
        return super().sum_attrs() + self.attr_3 + self.attr_4