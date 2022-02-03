from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def fabric_calculation(self):
        pass

    def __add__(self, other):
        return f'Суммарный расход ткани на пошив, ' \
               f'заявленного количества пальто и костюмов, составит {self.sum + other.sum} метров'


class Coat(Clothes):
    def __init__(self, amount, v):
        super().__init__(amount)
        self.v = v/6.5 + 0.5
        self.sum = round(self.amount*self.v, 2)

    @property
    def fabric_calculation(self):
        return f'Для пошива {self.amount} штук пальто необходимо {self.sum} метров ткани'


class Costume(Clothes):
    def __init__(self, amount, h):
        super().__init__(amount)
        self.h = 2*h + 0.3
        self.sum = round(self.amount*self.h, 2)

    @property
    def fabric_calculation(self):
        return f'Для пошива {self.amount} штук костюмов необходимо {self.sum} метров ткани'


coat = Coat(85, 46)
print(coat.fabric_calculation)

costume = Costume(95, 48)
print(costume.fabric_calculation)

print(coat + costume)
