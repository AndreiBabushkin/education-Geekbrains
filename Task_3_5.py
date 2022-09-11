"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
Fn = F(n+2)−F(n+1)
Fn = Fn-1 + Fn-2"""
n = int(input('Введите число '))

n_fib1 = 0
n_fib2 = 1

list_f = [n_fib2, n_fib1, n_fib2]

for x in range(0, n - 1):
    n_fib1, n_fib2 = n_fib2, n_fib1 + n_fib2
    if x % 2 == 0:
        list_f.append(-n_fib2)
    else:
        list_f.append(n_fib2)

fib1 = 0
fib2 = 1

list_f.reverse()

for i in range(0, n-1):
    fib1, fib2 = fib2, fib1 + fib2
    list_f.append(fib2)
print(list_f)


