class Zerodivision(Exception):
    def __str__(self):
        return 'На ноль делить нельзя'


a = int(input('Введите число которое хотите разделить: '))
b = int(input('Введите число на которое хотите разделить: '))

try:
    c = a/b
except ZeroDivisionError:
    print(Zerodivision())
else:
    print('Результат:', c)
