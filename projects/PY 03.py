#1 Создание списка строк:
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

#2 Создание алгоритма заполнения словаря для любой строчки лога:
def log(i):
    list_split = list[int(i)].split()
    dict = {'time': " ".join(list_split[:3]), 'pc_name': list_split[3], 'service_name': (list_split[4])[:-1], 'message': " ".join(list_split[5:])}
    return dict

#3.1 Запрос номера строки:
i = input(f"Выберите, пожалуйста, номер строки списка (между 0-{(len(list)-1)}): ")

#3.2 Вывод на экран <имя компьютера> и <сообщение>, исходя из номера строки:
lineselect = log(i)
print(lineselect['pc_name'] + ": " + lineselect['message'])

#4.1 Новый литерал списка: 
listnew = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']

#4.2 Создание списка ключей нового списка:
keys = ['time','pc_name','service_name','message']

#4.3 Создание словаря из двух списков:
dictnew = dict(zip(keys, listnew))
#print(dictnew)

#5 Создание списка словарей (объединение):
oldnew = [lineselect, dictnew]
print(f"Создание списка словарей (объединение): {oldnew}")


#6.1 Вывод одинаковых значений:

lineselect1 = set(lineselect.values())
dictnew1 = set(dictnew.values())
print(f"Совпадение значения:  {lineselect1 & dictnew1}")

#6.2 Вывод одинаковых значений (предыдущий вариант):
print(f"Совпадение ключ-значение: {dict(set(dictnew.items()) & set(lineselect.items()))}")