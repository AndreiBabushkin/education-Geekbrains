"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19"""
import random


list_1 = [round(random.uniform(0, 10), 2) for i in range(5)]
print(list_1)
list_2 = []
for x in list_1:
    if x % 1 != 0:
        list_2.append(x % 1)
print(round(max(list_2) - min(list_2), 2))
