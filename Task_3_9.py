"""Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
import random

matrix = [[random.randint(1, 100) for i in range(5)] for y in range(5)]
for m in matrix:
    print(m)
max_list = []
for i in range(5):
    min_list = []
    for j in range(5):
        min_list.append(matrix[j][i])
    max_list.append(min(min_list))
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы {max(max_list)}')
