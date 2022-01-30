class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position
        self._income = {"Оклад": wage, "Премия": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника - {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии - {sum(self._income.values())}$')

Andrei = Position('Андрей', 'Бабушкин', 'Дворник', 250, 50)
Andrei.get_total_income()
Andrei.get_full_name()
print(Andrei.name)
print(Andrei.surname)
print(Andrei.position)
print(Andrei._income)

Masha = Position('маша', 'бабушкина', 'Мастер', 750, 25)
Masha.get_total_income()
Masha.get_full_name()

print(Masha.name)
print(Masha.surname)
print(Masha.position)
print(Masha._income)