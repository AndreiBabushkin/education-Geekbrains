"""Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N"""
list_a = []


def is_prime(x):

    for i in range(2, (x//2)+1):
        if x % i == 0:
            list_a.append(i)
            return is_prime(int(x / i))
    return list_a.append(x)


n = int(input('Введите число: '))
is_prime(n)
print(list_a)
