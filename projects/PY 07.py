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
#  - сколько угодно строк логов по типу тех, что есть в скопированном вами списке.

class names:
    n: int
    num: int
    i: int
    z: int
    k: int

k: names = len(list) - 1

n = int(input(f'Сколько будет строк логов? '))

num: names = 0 
newlist = []
enter = []
l = []
while num < n: 
    num = num + 1
    enter = input(f'Введите строку № {num} лога, без кавычек (пример -  May 20 11:01:12 PC-00102 PackageKit: daemon start  ): ')
    newlist.append(enter)

def func(l, *args):
    l.extend(*args) 
    return(l)

list = (func(list, newlist))
  

# 2.2. Превращает вводимые вами строки логов в словари по тому же принципу, что и в пункте 2 задания для 3го урока.

# Вывод только нового лога/словаря:

print('Вывод только нового лога:')

i: names = 0
def lognew(i):
    list_split = newlist[int(i)].split()
    dict = {'time': " ".join(list_split[:3]), 'pc_name': list_split[3], 'service_name': (list_split[4])[:-1], 'message': " ".join(list_split[5:])}
    return dict

while i < n:
    lognew(i)
    print(lognew(i))
    i = i + 1


#2.3. Модифицирует входной список (переданный в качестве первого аргумента), добавляя в него все созданные словари. 
#  Возвращать функция, соответственно, должна None

# Вывод полного списка: и старого лога/словаря, и нового:

def log(i):
    list_split = list[int(i)].split()
    print({'time': " ".join(list_split[:3]), 'pc_name': list_split[3], 'service_name': (list_split[4])[:-1], 'message': " ".join(list_split[5:])})


print('Вывод и старого, и нового лога:')
z: names = k + n
i: names = 0
while i < z:
    log(i)
    i = i + 1

# Возвращение функции None
print(log(i))
