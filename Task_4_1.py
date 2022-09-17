"""Вычислить число c заданной точностью d
Пример:
при d = 0.001, π = 3.141        10-1 <= d <= 10-10"""
import math


while True:
    d = input('Введите число с точностью в 10**-10 <= d <= 10**-1')
    if 10**-10 <= float(d) <= 10**-1:
        num = 0
        for i in str(d):
            if i.isdigit():
                num += 1
        print(round(math.pi, num - 1))
        break
