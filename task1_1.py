"""Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

integer = input('Введите трехзначное число: ')
summa = int(integer[0]) + int(integer[1]) + int(integer[2])
proz = (int(integer[0]) * int(integer[1]) * int(integer[2]))

print('Сумма цифр введенного числа:', summa)
print('Произведение цифр введенного числа:', proz)

