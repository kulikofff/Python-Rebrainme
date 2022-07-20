'''
sum_1 = 0
num_1 = input('Введите слагаемое или нажмите Enter для вычисления суммы: ')
while num_1:
    try:
        sum_1 += float(num_1)
    except ValueError:
        print('Вы ввели не число')
    num_1 = input('Введите слагаемое или нажмите Enter для вычисления суммы: ')
print(f'Сумма чисел равна {str(sum_1)}')



list_1 = [1, 2, 3]
try:
    num_1 = float(input('Введите делимое: '))
    num_2 = float(input('Введите делитель: '))
    try:
        pos = int(input('Введите позицию для записи: '))
        list_1[pos] = num_1 / num_2
        print(list_1)
    except IndexError:
        list_1[-1] = num_1 / num_2
        print('Указанная вами позиция не существует. Число было записано на последнюю доступную позицию')
    except ZeroDivisionError:
        list_1[pos] = num_1
        print('Делитель равен нулю. Записывается только делимое')
except ValueError:
    print('Вы ввели не число. Операция отклонена')


try:
    raise ValueError('Wrong value', 25)
except ValueError as a:
    print(a.args[0])
    print(a)


class MyException(Exception):
    def __init__(self, info):
        MyException.info = info

try:
    raise MyException('Test_message')
except MyException as Except_instance:
    print(Except_instance) # Выведет 'Test_message'
'''

class MyException(ValueError):
    pass

try:
    raise MyException
except ValueError:
    print('Ошибка')