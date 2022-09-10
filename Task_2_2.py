"""Написать программу получающую набор произведений чисел от 1 до N.
Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]"""
import random


proz = 1
list_num = []
for i in range(1, random.randint(1, 25)):
    print(i)
    proz *= i
    list_num.append(proz)
print(list_num)
