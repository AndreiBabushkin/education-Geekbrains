class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Гелевая {self.title} синевого цвета')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} графитовый, мягкий')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} по металлу')

pen = Stationery('ручка')
pen.draw()
pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()
