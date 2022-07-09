#1. Список:
disks: list = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]

#2. Функция - словарь вида {'id': <id устройства>, 'memory_status': <статус памяти>}.
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
    

#print(*storage_analyzer(disks))

#3.  Формирование списка словарей статусов накопителей и объединние этих словарей со словарями из основного списка:

[a.update(b) for a, b in zip(disks, storage_analyzer(disks))]

#4. Вывод итогового списка словарей на экран:

print('Вывод итогового списка словарей на экран:')
print()
for i in disks:
    print(i)
print()
#6. Используя лямбда-функцию отсортируйте этот список по времени (не по дате/времени) и выведите 3й 
# элемент отсортированного списка.

loglist = ['May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
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


print('3-й элемент отсортированного списка:')
newloglist = sorted(loglist, key=lambda a: a.split()[2])
print(newloglist[2])
print()

#7. Используя функцию filter() или списковые включения, сформируйте новый список, в который входят только логи,
# которые записал PC-00102.

loglist102 = [i for i in loglist if i.split()[3] == 'PC-00102']

print('Логи, которые записал PC-00102:')
print(loglist102)
print()

#8. Используя списковые включения, сформируйте список сообщений логов, которые записал процесс kernel. 
# Необходимо составить список только из сообщений. Дату, время, имя ПК и имя сервиса включать не нужно.

loglistkernel: list = [i for i in loglist if i.split()[4] == 'kernel:']
loglistkernel1: list = (a for a in map(lambda a: a.split(': ', 1), loglistkernel))

print('Cписок сообщений логов, которые записал процесс kernel:')
for n in loglistkernel1:
    print(n[1])
