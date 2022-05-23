"""В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться"""
import random


list_1 = [random.randint(-1, 20) for i in range(10)]
print(list_1)

min_1 = list_1.index(min(list_1))
print(f'Первое минимальное число {min(list_1)}')
list_1.remove(list_1[min_1])
print(f'Второе минимальное число {min(list_1)}')