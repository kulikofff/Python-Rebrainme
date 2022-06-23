print('FIRST TASK:')

s1 = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'

print(f'Date is {s1[0:15]}')
print(f'Service name is {s1[24:34]}')
pc = 'PC-12092'
print(f'May 24 12:48:31 {pc} systemd[1]: logrotate.service: Succeeded.')
failed = (s1.find('failed'))
print(f'Failed found = {failed}')
S = s1.upper()
SS = S.count('S')
print(f'Number of s or S = {SS}')

HH = s1[7:9]
MM = s1[10:12]
SS = s1[13:15]

sum = int(HH) + int(MM) +int(SS)
print(f'HH+MM+SS = {sum}')

print('SECOND TASK:')

s2 = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'

namePC = s2[16:23]
nameS = s2[24:35]
text = s2[37:69]
reason = s2[71:91]
time = s2[0:15]

print(f'The PC "{namePC}" receive message from service "{nameS}" what says "{text}" because "{reason}" at "{time}"')