class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.speed > 0:
            print(f'Машина {self.name} поехала. Это полицейская машина? {self.is_police}')

    def stop(self):
        if self.speed == 0:
            print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        if self.direction == 'направо':
            print(f'Машина {self.name} повернула направо')
        elif self.direction == 'налево':
            print(f'Машина {self.name} повернула налево')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости', self.name, 'на', self.speed - 60, 'км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed} км/ч')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости', self.name, 'на', self.speed - 40, 'км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed} км/ч')

mazda = Car(40, 'белый', 'Mazda', None)
mazda.go()
mazda.stop()
mazda.turn('налево')
audi = TownCar(80, 'черный', 'Audi', None)
audi.show_speed()
audi.go()
bugatti = SportCar(180, 'красный', 'Bugatti', None)
bugatti.show_speed()
fiat = WorkCar(48, 'белый', 'Fiat', None)
fiat.show_speed()
toyota = PoliceCar(87, 'черный', 'Toyota', 'да')
toyota.go()
toyota.show_speed()
print(toyota.is_police)
print(bugatti.color)
print(audi.name)