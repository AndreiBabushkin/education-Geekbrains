""" Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»"""
import cProfile


n = 9999999
a = [0] * n
for i in range(n):
    a[i] = i
a[1] = 0
m = 2
while m < n:
    if a[m] != 0:
        j = m * 2
        while j < n:
            a[j] = 0
            j = j + m
    m += 1
b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])
del a

num_i = int(input('Какое по счету ищете простое число? Введите: '))
cProfile.run("print(f'{num_i} по счету простое число это {b[num_i - 1]}')")
"""0 по счету простое число это 29
         4 function calls in 0.010 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.010    0.010    0.010    0.010 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""

def search_number(n):
    count = 1
    number = 1
    prime_number = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime_number:
            if number % num == 0:
                break
        else:
            count += 1
            prime_number.append(number)

    return number

cProfile.run("print(search_number(10))")

"""  104 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 Test.py:3(search_number)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""


"""В первом предложеном мной варианте решения (с использованием «Решето Эратосфена») задача имеет линейную сложность
 и зависти от длины составляемого списка. Поиск числа по индексу элемента это О(1). Данный способ уместно использовать 
 при многократном поиске чисел за счет большей скорости работы кода по сравнению со вторым вариантом.
 Во втором варианте решения алгоритм имеет квадратичную сложность, т. к. при увеличении числа в 10 раз увеличивается 
 время на его поиск примерно в 100 раз. Данный алгоритм уместнее использовать для опимизации объема используемой 
 памяти"""