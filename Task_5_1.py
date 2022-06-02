"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего."""
import collections


n = int(input('Введите кол-во предприятий: '))
dct = {}
for _ in range(n):
    name_com = input('Введите название компании: ')
    profit_year = []
    for profit in range(1, 5):
        profit_year.append(float(input(f'Укажите прибыль {name_com} за {profit} квартал: ')))
    profit_year = sum(profit_year)
    dct[name_com] = profit_year
average_profit = sum(dct.values())/n
below_the_average = collections.deque()
above_average = collections.deque()
for company in dct:
    if dct[company] > average_profit:
        below_the_average.append(company)
    if dct[company] < average_profit:
        above_average.append(company)

print(f'Средняя прибыль за год для всех предприятий составляет: {average_profit}')
print(f'Компании с годовой прибылью ниже среднего - {", ".join(below_the_average)}')
print(f'Компании с годовой прибылью выше среднего - {", ".join(above_average)}')
