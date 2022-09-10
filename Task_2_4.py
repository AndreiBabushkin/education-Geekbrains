"""Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6])."""
import random

list_num = []
positions = [1, 3, 6]

num = int(input('Введите число: '))
for i in range(-num, num+1):
    list_num.append(i)
print(list_num)

# for x in range(random.randint(1, len(list_num)+1)):
#     positions.append(random.randint(0, len(list_num)))
# print(positions)

proz = 1
while len(positions) != 0:
    proz *= (list_num[positions[-1]])
    del positions[-1]
print(proz)
