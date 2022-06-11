"""Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее)"""
import random


def bubble_sort(array):

    for i in range(n-1):
        for j in range(n-i-1):
            if array[j+1] > array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


n = 30
list_1 = [random.randint(-100, 100) for i in range(n)]
print(list_1)

print(bubble_sort(list_1))

