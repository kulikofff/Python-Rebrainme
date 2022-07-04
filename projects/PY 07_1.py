
list = ['May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
'May 20 11:01:12 PC-00102 PackageKit: daemon start',
'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.']

# 2.1. Получает в качестве первого аргумента список для вывода данных, а в качестве последующих
# - сколько угодно строк логов по типу тех, что есть в скопированном вами списке.
# 2.2. Превращает вводимые вами строки логов в словари по тому же принципу, что и в пункте 2 задания для 3го урока.
# 2.3. Модифицирует входной список (переданный в качестве первого аргумента), добавляя в него все созданные словари. Возвращать функция, соответственно, должна None

def log_parse(string: str):
    result: dict = {}

    *time, pc_name, service = string.split(" ", 4)
    result["time"] = " ".join(time)
    result["pc_name"] = pc_name
    result["service_name"], result["message"] = service.split(": ", 1)
    return result

def logger_append(log_list: list, *args):
    for arg in args:
        log_list.append(log_parse(arg))
    return

#3. Создайте пустой список и добавьте в него 1ю, 2ю и 4ю запись из списка логов с помощью одного вызова вашей функции. Выведите полученный список на экран

list_log: list = []

logger_append(list_log, list[0], list[1], list[3])

print('Вывод списка с 1,2,4 записями:')

for log in list_log:
    print(log)


#4. Скопируйте к себе этот модифицированный список из 4го урока, отображающий количество общей и занятой памяти на накопителях:

disks: list = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]

#5.2., 5.3 Анализ состояния памяти каждого накопителя по алгоритму из задания для 4го урока. 
# Формирует словарь, ключами которого являются: 'memory_ok', 'memory_not_enough' и 'memory_critical', а значениями - списки id накопителей,
# состояние которых относится к соответствующему ключу. 5.4. Возвращает сформированный словарь.

def storage_analyzer(disk_list: list):
    disks_dictionary = dict()
    memory_ok: list = []
    memory_not_enough: list = []
    memory_critical: list = []

    for i in disk_list:
        free_space: int = i['total'] - i['used']
        free_space_percent: float = free_space*100/i['total']
        free_space_in_gb: float = free_space / 1024 ** 3

        if free_space_percent <= 5 or free_space_in_gb <= 10:
            memory_critical.append(i['id'])
        elif free_space_percent <= 10 or free_space_in_gb <= 30:
            memory_not_enough.append(i['id'])
        else:
            memory_ok.append(i['id'])

    disks_dictionary['memory_critical'] = memory_critical
    disks_dictionary['memory_not_enough'] = memory_not_enough
    disks_dictionary['memory_ok'] = memory_ok

    return disks_dictionary


#6. Примените эту функцию к вашему списку и выведите словарь, полученный в результате ее работы, на экран.

print('Вывод словаря:')

print(storage_analyzer(disks))
