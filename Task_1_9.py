'''Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).'''
x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))
x3 = int(input('Введите третье число: '))

if (x3 > x1 > x2) or (x3 < x1 < x2):
    print(x1, '- среднее число')
elif (x1 > x2 > x3) or (x1 < x2 < x3):
    print(x2, '- среднее число')
elif x1 == x2 or x3 == x1 or x2 == x3:
    print('Введите разные числа')
else:
    print(x3, '- среднее число')
