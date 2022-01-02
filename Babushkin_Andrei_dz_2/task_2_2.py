weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
temp_morning = []
for number in weather:
    if number.isdigit():
        number = number.zfill(2)
        number = f'"{number}"'
        temp_morning.append(number)
    elif number.startswith('+') and len(number) < 3:
        for degree in number:
            if degree.isdigit():
                degree = '+' + degree.zfill(2)
                degree = f'"{degree}"'
                temp_morning.append(degree)
    elif number.startswith('-') and len(number) < 3:
        for degree in number:
            if degree.isdigit():
                degree = '-' + degree.zfill(2)
                degree = f'"{degree}"'
                temp_morning.append(degree)
    elif number.startswith('-') or number.startswith('+'):
        number = f'"{number}"'
        temp_morning.append(number)
    else:
        temp_morning.append(number)
temp_morning = ' '.join(temp_morning)
print(temp_morning)

