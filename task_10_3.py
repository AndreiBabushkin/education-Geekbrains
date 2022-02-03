class Cell:
    def __init__(self, number_of_cells):
        self.cell = number_of_cells

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell > other.cell:
            return self.cell - other.cell
        else:
            return f'значение меньше либо равно 0'

    def __floordiv__(self, other):
        return self.cell // other.cell

    def __truediv__(self, other):
        return self.cell / other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def make_order(self, number_in_line):
        one_list = []
        while self.cell != 0:
            one = self.cell/self.cell
            one = '*'
            one_list.append(one)
            self.cell -= 1
        i = number_in_line
        while i < len(one_list):
            one_list.insert(i, '\n')
            i += number_in_line + 1
        return ''.join(one_list)


c = Cell(100)
c1 = Cell(28)
print(c + c1)
print(c - c1)
print(c // c1)
print(c / c1)
print(c * c1)
print(c.make_order(18))
