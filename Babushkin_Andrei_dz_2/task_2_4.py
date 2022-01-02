personal = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in personal:
    i = i.title()
    position_name = i.split(' ')
    print('Привет,', position_name[-1]+'!')
