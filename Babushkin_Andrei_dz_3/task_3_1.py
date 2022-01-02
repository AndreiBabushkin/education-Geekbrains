def num_translate(number):
    if number == 'zero':
        return '"ноль"'
    elif number == 'one':
        return '"один"'
    elif number == 'two':
        return '"два"'
    elif number == 'three':
        return '"три"'
    elif number == 'four':
        return '"четыре"'
    elif number == 'five':
        return '"пять"'
    elif number == 'six':
        return '"шесть"'
    elif number == 'seven':
        return '"семь"'
    elif number == 'eight':
        return '"восемь"'
    elif number == 'nine':
        return '"девять"'
    elif number == 'ten':
        return '"десять"'
    return None

print(num_translate('zero'))

