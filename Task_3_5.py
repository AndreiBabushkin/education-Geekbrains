"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""
import random


list_1 = [random.randint(-10, 3) for i in range(15)]
print(list_1)

position = None
num = 0
for min_n in list_1:
    if min_n < num:
        num = min_n
for i, val in enumerate(list_1):
    if val > num and val < 0:
        num = val
        position = i + 1
print(f'Максимальный отрицательный элемент в массиве равен {num} находится на {position} позиции')
