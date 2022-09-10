"""Задать список из n чисел последовательности (1 + 1/n)^n и вывести на экран их сумму."""
import random

list_n = []

for i in range(1, random.randint(2, 10)):
    list_n.append((1+1/i)**i)
print(list_n)
print('сумма послеовательности чисел =', sum(list_n))
