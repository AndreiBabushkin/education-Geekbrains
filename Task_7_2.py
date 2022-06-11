"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы"""
import random


def merge_sort(array):
    if len(array) <= 1:
        return array

    right = merge_sort(array[len(array) // 2:])
    left = merge_sort(array[:len(array) // 2])
    i = 0
    j = 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1

    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


n = 25
list_1 = [random.randint(0, 50) for i in range(n)]
print(list_1)

print(merge_sort(list_1))
