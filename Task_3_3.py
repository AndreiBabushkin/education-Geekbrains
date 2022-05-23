"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы"""
import random

list_1 = [random.randint(1, 100) for i in range(10)]
print(list_1)
max_n = max(list_1)
min_n = min(list_1)
print(f'Максимальный элемент массива {max(list_1)}')
print(f'Минимальный элемент массива {min(list_1)}')
for i, val in enumerate(list_1):
    if val == max_n:
        list_1[i] = min_n
    if val == min_n:
        list_1[i] = max_n
print(list_1)
