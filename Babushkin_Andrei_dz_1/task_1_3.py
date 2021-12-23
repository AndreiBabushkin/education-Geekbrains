for number in range(1, 101):
    if number % 10 == 1 and number != 11:
        print(number, 'процент')
    elif number % 10 > 1 and number % 10 < 5 and number != 12 and number != 13 and number != 14:
        print(number, 'процента')
    else:
        print(number, 'процентов')