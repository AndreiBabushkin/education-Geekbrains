"""Определить, какое число в массиве встречается чаще всего."""
import random


list_1 = [random.randint(1, 5) for i in range(15)]
print(list_1)

num = 0
count = 0

for i in list_1:
    q = list_1.count(i)
    if q > count:
        count = q
        num = i
print(f'{count} раза встречается число {num}')
