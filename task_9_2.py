class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width
        self.mass = 25
        self.hight = 5
        self.mass_of_asphalt = self._lenght * self._width * self.mass * self.hight/1000

    def definition_of_mass_of_asphalt(self):

        print(f'{self._lenght} м*{self._width} м*{self.mass} кг*{self.hight} см = {round(self.mass_of_asphalt)} т.')

m = Road(20, 5000)

n = Road(100, 2500.2)
m.definition_of_mass_of_asphalt()
n.definition_of_mass_of_asphalt()
