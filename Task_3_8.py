"""Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
 Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
 В конце следует вывести полученную матрицу"""
matrix = []


def func():
    list_m = []
    for n in range(3):
        list_m.append(int(input('Введите число: ')))
    list_m.append(sum(list_m))
    return list_m


for i in range(5):
    matrix.append(func())

print(matrix)
