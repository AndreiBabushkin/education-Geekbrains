class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def conversion_to_type_number(cls, date):
        date_number = [int(i) for i in date.split('-')]
        return f'День - {date_number[0], type(date_number[0])},Месяц - {date_number[1], type(date_number[1])}, ' \
               f'Год - {date_number[2], type(date_number[2])}'

    @staticmethod
    def valid_number(date):
        date_number, month, year = [int(i) for i in date.split('-')]
        if date_number < 0 and date_number > 31:
            raise TypeError('Введен не существующий день')
        elif month < 0 and month > 12:
            raise TypeError('Введен не существующий месяц')
        elif year < 1:
            raise TypeError('Введен не существующий год')
        else:
            return f'День - {date_number},Месяц - {month}, Год - {year}'


d = Date('13-03-1988')
print(d.conversion_to_type_number('23-01-2018'))
print(d.valid_number('05-12-2020'))
