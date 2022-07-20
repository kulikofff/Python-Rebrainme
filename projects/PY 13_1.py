class PercentError(Exception):
    pass


class PC_memory:
    def __init__(self, pc_id: str, user_name: str, memory_total: int, memory_used: int, memory_percent: float = None):
        self.pc_id = pc_id
        self.user_name = user_name

        try:
            self.memory_total = int(memory_total)
            self.memory_used = int(memory_used)
            if self.memory_total < 0 or self.memory_used <0 or self.memory_used > self.memory_total:
                raise ValueError
        except ValueError:
            print("Wrong memory value, default value used")
            self.memory_total = 100*1024**3
            self.memory_used = 0
            self.memory_percent = 0
            
        if memory_percent:
            try:
                self.memory_percent = float(memory_percent)
                if self.memory_percent < 0 or self.memory_percent > 100:
                    raise PercentError('Percent value must be between 0 and 100')
            except PercentError:
                print("Wrong percent value, value calculated automatically")
                self.memory_percent = self.memory_used*100/self.memory_total
        else:
            self.memory_percent = self.memory_used*100/self.memory_total

    def show_used_percent(self):

        print(f'PC with id {self.pc_id} used {self.memory_percent:2.0f} percent of memory')
        print(self.memory_total)
        print(self.memory_used)

    def is_enough_memory(self):
        if self.memory_percent < 10:
            return False
        else: 
            return True


print('\n1. Нечисловая строка:')
info_pc_env = PC_memory('AVK_PC', 'AVK-PC', 'string', 100)

print('\n2. Слишком большое количество используемой памяти:')
info_pc_env = PC_memory('AVK_PC', 'AVK-PC', 50, 100)

print('\n3. Отрицательное значение памяти')
info_pc_env = PC_memory('AVK_PC', 'AVK-PC', -50, -10)

print('\n4. Некорректный процент занятой памяти')
info_pc_env = PC_memory('AVK_PC', 'AVK-PC', 100, 50, 140)

print('\n4. Корректные и полные данные')
info_pc_env = PC_memory('AVK_PC', 'AVK-PC', 100, 60, 60)


