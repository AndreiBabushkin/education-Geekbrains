"""Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""
sixteen_sys = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
               'D': 13, 'E': 14, 'F': 15, 'G': 16}


def mass(x):

    mass_int = []
    for i in x:
        mass_int.append(i)
    return mass_int


def decimalization(y):
    dcml = []
    for dcml_int in y:
        dcml.append(sixteen_sys.get(dcml_int))
    for ind, val in enumerate(dcml[::-1]):
        dcml[ind] = val * 16 ** ind
    return sum(dcml)


def hexadecimal_conversion(z):
    hex_int = []
    while z != 0:
        remainder = z % 16
        hex_int.append(remainder)
        z //= 16
    hex_int_2 = []
    for c in hex_int[::-1]:
        for k, v in sixteen_sys.items():
            if v == c:
                hex_int_2.append(k)
    return hex_int_2


first_int = input('Введите первое шестнадцатиричное число: ').upper()
second_int = input('Введите второе шестнадцатиричное число: ').upper()

sum_dcml = decimalization(mass(first_int)) + decimalization(mass(second_int))
proz_dcml = decimalization(mass(first_int)) * decimalization(mass(second_int))

print(hexadecimal_conversion(sum_dcml))
print(hexadecimal_conversion(proz_dcml))
