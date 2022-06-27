import copy

#1. Создание списка строк:
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

#2. Создание списка словарей:
def log(i):
    list_split = list[int(i)].split()
    dict = {'time': " ".join(list_split[:3]), 'pc_name': list_split[3], 'service_name': (list_split[4])[:-1], 'message': " ".join(list_split[5:])}
    return dict

lineselect: list = []
i = 0
for num in list:  
    lineselect.append(log(i))
    i = i + 1
print(lineselect)
print()

#3. Cписок значений <дата/время> всех словарей, используя списковое включение:

listtime=copy.deepcopy(lineselect)
listtime = [i['time'] for i in listtime]
print(listtime)
print()

#4. Измените словари в списке: создайте новый ключ 'date', перенеся в его значение дату из поля 'time'.
#  В поле 'time' оставьте только время. Выведите значения для поля 'time' всех словарей в списке.

lineselect2=copy.deepcopy(lineselect)

for i in lineselect2:
    *date, i['time'] = i['time'].split(" ", 2)
    i['date'] = ' '.join(date)
    print(f"{i['time']}")
print() 

#5 Выведите список значений поля 'message' для всех логов, которые записал ПК с именем 'PC0078':

logs: list = []
logs = [i['message'] for i in lineselect2 if i['pc_name'] == 'PC0078']
print(logs)
print()

#6. Превратите список словарей логов (который вы сделали в задании 2) в словарь.
#   Ключами в нем будут целые числа от 100 до 110, а значениями - словари логов.
vocab = {}
vocab = (dict(enumerate(lineselect, start=100)))

#7 Выведите на экран словарь лога под ключом 104.
print(f"Key: 104 | Value: {vocab[104]}")

