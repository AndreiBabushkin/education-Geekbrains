from abc import ABC


class Value(Exception):
    def __str__(self):
        return 'Введено не число'


class Warehouse(ABC):
    def number(self):
        pass


class Officeequipment:
    def __init__(self, model, number):
        self.model = model
        try:
            self.number = int(number)
        except ValueError:
            print(Value())

    def __str__(self):
        try:
            return f'Текущий остаток {self.model}: {self.number} штук'
        except AttributeError:
            print('Не верно указан атрибут')


class Printer(Officeequipment):
    def __init__(self, model, number, print_speed):
        super().__init__(model, number)
        self.print_speed = print_speed

    def __str__(self):
        try:
            return f'Текущий остаток {self.model}: {self.number} штук'
        except AttributeError:
            print('Не верно указан атрибут')

    def __add__(self, other):
        remainder_dict = {}
        if self.model == other.model and self.print_speed == other.print_speed:
            remainder = self.number + other.number
            remainder_dict[self.model] = (self.print_speed, remainder)
            return f'Поступило на склад {other.number}. Текущий остаток {remainder_dict} штук'
        else:
            remainder_dict[self.model] = (self.print_speed, self.number)
            remainder_dict[other.model] = (other.print_speed, other.number)
            return f'Текущий остаток {remainder_dict} штук'

    def __sub__(self, other):
        remainder_dict = {}
        if self.model == other.model and self.print_speed == other.print_speed:
            remainder = self.number - other.number
            remainder_dict[self.model] = (self.print_speed, remainder)
            return f'Передано в подразделение {other.number}. Текущий остаток {remainder_dict} штук'
        else:
            remainder_dict[self.model] = (self.print_speed, self.number)
            remainder_dict[other.model] = (other.print_speed, other.number)
            return f'Текущий остаток {remainder_dict} штук'


class Scaner(Officeequipment):
    def __init__(self, model, number, scan_speed):
        super().__init__(model, number)
        self.scan_speed = scan_speed

    def __str__(self):
        try:
            return f'Текущий остаток {self.model}: {self.number} штук'
        except AttributeError:
            print('Не верно указан атрибут')

    def __add__(self, other):
        remainder_dict = {}
        if self.model == other.model and self.scan_speed == other.scan_speed:
            remainder = self.number + other.number
            remainder_dict[self.model] = (self.scan_speed, remainder)
            return f'Поступило на склад {other.number}. Текущий остаток {remainder_dict} штук'
        else:
            remainder_dict[self.model] = (self.scan_speed, self.number)
            remainder_dict[other.model] = (other.scan_speed, other.number)
            return f'Текущий остаток {remainder_dict} штук'

    def __sub__(self, other):
        remainder_dict = {}
        if self.model == other.model and self.scan_speed == other.scan_speed:
            remainder = self.number - other.number
            remainder_dict[self.model] = (self.scan_speed, remainder)
            return f'Передано в подразделение {other.number}. Текущий остаток {remainder_dict} штук'
        else:
            remainder_dict[self.model] = (self.scan_speed, self.number)
            remainder_dict[other.model] = (other.scan_speed, other.number)
            return f'Текущий остаток {remainder_dict} штук'


class Xerox(Officeequipment):
    def __init__(self, model, number, copy_number):
        super().__init__(model, number)
        self.copy_number = copy_number

    def __str__(self):
        try:
            return f'Текущий остаток {self.model}: {self.number} штук'
        except AttributeError:
            print('Не верно указан атрибут')

    def __add__(self, other):
        remainder_dict = {}
        if self.model == other.model and self.copy_number == other.copy_number:
            remainder = self.number + other.number
            remainder_dict[self.model] = (self.copy_number, remainder)
            return f'Поступило на склад {other.number}. Текущий остаток {remainder_dict} штук'
        else:
            remainder_dict[self.model] = (self.copy_number, self.number)
            remainder_dict[other.model] = (other.copy_number, other.number)
            return f'Текущий остаток {remainder_dict} штук'

    def __sub__(self, other):
        remainder_dict = {}
        if self.model == other.model and self.copy_number == other.copy_number:
            remainder = self.number - other.number
            remainder_dict[self.model] = (self.copy_number, remainder)
            return f'Передано в подразделение {other.number}. Текущий остаток {remainder_dict} штук'
        else:
            remainder_dict[self.model] = (self.copy_number, self.number)
            remainder_dict[other.model] = (other.copy_number, other.number)
            return f'Текущий остаток {remainder_dict} штук'


p = Printer('A589', 12, '60 листов')
p1 = Printer('A589', 10, '60 листов')
s = Scaner('S234', 58, '25 листов')
s1 = Scaner('S233', 5, '15 листов')
x = Xerox('X2', 58, '25 листов')
x1 = Xerox('X2', 5, '25 листов')

print(p)
print(p+p1)
print(p-p1)
print(s+s1)
print(s-s1)
print(x + x1)
print(x - x1)
