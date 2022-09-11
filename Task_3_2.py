"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

import random


list_1 = [random.randint(0, 10) for i in range(5)]
print(list_1)
list_proz = []
for x in list_1:
    list_proz.append(x*list_1.pop())
print(list_proz)