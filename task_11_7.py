class Complexnumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __truediv__(self, other):
        return self.number / other.number


z1 = Complexnumber(15+5j)
z2 = Complexnumber(5-3j)
z = Complexnumber(-1-1j)
print(z1 + z2)
print(z1 / z2)
print(z + z2)
print(z1 / z)
