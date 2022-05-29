""" Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их"""
import cProfile


"""Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""
integer = input('Введите трехзначное число: ')
summa = int(integer[0]) + int(integer[1]) + int(integer[2])
proz = int(integer[0]) * int(integer[1]) * int(integer[2])

cProfile.run("print('Сумма цифр введенного числа:', summa), print('Произведение цифр введенного числа:', proz) ")

"""Введите трехзначное число: 895
Сумма цифр введенного числа: 22
Произведение цифр введенного числа: 360
         5 function calls in 0.332 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.331    0.331    0.332    0.332 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""

integer = input('Введите трехзначное число: ')
summa = 0
proz = 1
for i in integer:
    summa += int(i)
    proz *= int(i)
cProfile.run("print('Сумма:', summa, 'Произведение:', proz)")

"""Введите трехзначное число: 896
23 432
         4 function calls in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.007    0.007    0.007    0.007 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""

"""Представленная задача имеет линейную сложность, т. к. при скорость выполнения зависит от длины введенного числа.
При решении задачи через цикл и сохранении промежуточных данных в переменную достигается существенное увеличение 
в скорости"""
