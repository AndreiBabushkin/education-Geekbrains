"""Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k.
Пример:
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0"""
import random


k = int(input('Укажите степень: '))
list_k = [random.randint(0, 100) for _ in range(0, 3)]
with open('polynomial.txt', 'w', encoding='utf-8') as file_1:
    file_1.write(f'{list_k[1]}x**{k} + {list_k[0]}x + {list_k[2]}')
    print(f'{list_k[1]}x**{k} + {list_k[0]}x + {list_k[2]}')
