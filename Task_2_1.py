"""Подсчитать сумму цифр в вещественном числе."""
import random


float_num = random.uniform(0, 50)
print(float_num)
summ_num_float = 0
for num in str(float_num):
    if num.isdigit():
        summ_num_float += int(num)
print(summ_num_float)