def currency_rates(code_valute):

    import requests
    from decimal import Decimal

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    contains = response.text

    code_valute = code_valute.upper()

    if code_valute == 'USD':
        return (f'Курс доллара {contains[1659:1662]} к RUB составляет '
                f'{Decimal(float(contains[1723:1730].replace(",",".")))}')
    elif code_valute == 'EUR':
        return (f'Курс евро {contains[1799:1802]} к RUB составляет '
                f'{Decimal(float(contains[1857:1864].replace(",",".")))}')
    else:
        return None


print(currency_rates('eur'))