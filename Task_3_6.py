"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать."""
import random


list_1 = [random.randint(-1, 20) for i in range(10)]
print(list_1)

max_i = list_1.index(max(list_1))
min_i = list_1.index(min(list_1))
sum_n = 0
if max_i < min_i:
    max_i, min_i = min_i, max_i
for i in range(min_i + 1, max_i):
    sum_n += list_1[i]

print(f'Максимальное число {list_1[max_i]}, минимальное число {list_1[min_i]}')
print(f'Сумма чисел между минимальными и максимальными элементами {sum_n}')
