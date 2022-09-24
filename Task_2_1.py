"""Подсчитать сумму цифр в вещественном числе."""
import random


float_num = str(random.uniform(0, 50))
print(float_num)

# for num in str(float_num):
#     if num.isdigit():
#         summ_num_float += int(num)
print(sum(map(int, list(filter(str.isdigit, float_num)))))



