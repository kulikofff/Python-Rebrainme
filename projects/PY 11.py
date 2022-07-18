'''
class User:
    name = 'Иван'
    def set_name(self, name):
        self.name = name

a = User()
a.set_name('Виктория')
print(a.name)

User.set_name(a 'Виктория')


class User:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

a = User()
a.set_name('Григорий')
print(a.get_name())
'''

class User:
    def __init__(self, name):
        self.name = name
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

a = User('Дмитрий')
print(a.get_name())