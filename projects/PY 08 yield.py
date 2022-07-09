from typing import List

'''
def func():
    yield 1
    yield 2
    yield 3

print(func())

for u in func():
    print(u)

print(list(func()))
print(dict(enumerate(func(), start = 100)))

#def func_1(list_1):
#    for ugr in list_1:
#        yield ugr << 4

#for ugr in func_1([1,2,3,4]):
#    print(ugr)

def func_2(list1: List[str]) -> List[str]:
    list2 = []
    for ugr in list1:
        list2.append(ugr.upper()*2)
        list2.append(ugr.upper())
    return list2

print(func_2(['mm','dd','ff']))    
print(func_2.__annotations__) 


#func_list = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b]
#for func in func_list:
#    print(func(5, 2))

list_1 = [(1, 10), (2, 3), (4, 8), (10, 1)]
print(sorted(list_1, key=lambda a: a[1]))

list_1 = [-2, 10, 67]
list_2 = [5, 12, 1]
list_3 = list(map(lambda a, b: a * b, list_1, list_2))
print(list_3)

list_1 = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda a: (a ** 0.5).is_integer(), list_1)))


list_1 = [-2, 5, 120, -32, -9, 0]
print(list(abs(a) for a in list_1))

list_2 = [-2, 10, 67]
list_3 = [5, 12, 1]
print(list(a * b for a, b in zip(list_2, list_3)))

list_4 = [1, 2, 3, 4, 5, 6]
print(list(a for a in list_4 if (a ** 0.5).is_integer()))


def func():
    yield 1
    yield 2

#print(list(func()))
#print(*func())

for u in func():
    print(u)

############IT WORKS GOOG -> Просто функция

def gen_first(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(*gen_first(5))


############IT WORKS GOOG -> Круглые скобки
gen_first1 = (i + 3 for i in range(10))

print(*gen_first1)

##### lambda

lam : int = lambda a, b: a + b
print(lam(1,2))


list = ('29/10/21 23:55:11 192.168.0.1 GET 200 /python 1234', 
        '29/10/21 22:22:22 192.168.0.1 GET 200 /python?page=faq_buy 6664',
        '23/10/21 14:14:14 192.168.0.1 GET 200 /python?page=tasks 451')

# it works:

def log(*args):
    for i in args:
        yield list[i].split()
        
print(*log(0,1,2))
'''

disks: list = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]

def storage_analyzer(disk_list: list) -> list:

    for i in disk_list:
        free_space: int = i['total'] - i['used']
        free_space_percent: float = free_space*100/i['total']
        free_space_in_gb: float = free_space / 1024 ** 3

        if free_space_percent <= 5 or free_space_in_gb <= 10:
            memstat = 'memory_critical'
        elif free_space_percent <= 10 or free_space_in_gb <= 30:
            memstat = 'memory_not_enough'
        else:
            memstat = 'memory_ok'

    yield {"id": i['id'], "memory_status": memstat}


#3.  Формирование списка словарей статусов накопителей и объединние этих словарей со словарями из основного списка:

[a.update(b) for a, b in zip(disks, storage_analyzer(disks))]

#4. Вывод итогового списка словарей на экран:
for i in disks:
    print(i)