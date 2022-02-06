number_list = []
while True:
    class NumberError(Exception):
        def __str__(self):
            return 'Вы ввели не число'

    number = input('Введите число: ')

    if number == 'stop':
        break
    else:
        try:
            int(number)
            number_list.append(number)
        except ValueError:
            print(NumberError())

print(number_list)
