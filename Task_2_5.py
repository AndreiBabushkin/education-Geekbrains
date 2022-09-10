"""Реализовать алгоритм перемешивания списка."""
import random

list_1 = [i for i in range(10)]
print(list_1)

list_shuffle = []

for x in range(len(list_1)):
    list_shuffle.append(list_1.pop(random.randint(0, len(list_1)-1)))
print(list_shuffle)
