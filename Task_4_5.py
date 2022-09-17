"""Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
содержащий сумму многочленов."""

def sort_num(file):

    for i in file:
        if i.isdigit():
            list_digit.append(int(i))
        elif '**2' in i:
            list_x2.append(int(i[:i.find('**2') - 1]))
        elif i.find('x'):
            list_x.append(int(i[:i.find('x')]))


with open('sum_polynomial_1.txt', 'w', encoding='utf-8') as sum_p:
    with open('polynomial.txt', 'r', encoding='utf-8') as file_1:
        with open('polynomial_1.txt', 'r', encoding='utf-8') as file_2:
            list_x2 = []
            list_x = []
            list_digit = []
            sort_num(file_1.read().split(' + '))
            sort_num(file_2.read().split(' + '))
            sum_p.write(f'Сумма многочленов равна '
                        f'{sum(list_x2)}x**2 + {sum(list_x)}х + {sum(list_digit)}')
            print(f'{sum(list_x2)}x**2 + {sum(list_x)}х + {sum(list_digit)}')


