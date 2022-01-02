def thesaurus(*args):


    name_start_i = []
    name_start_p = []
    name_start_m = []
    for name in args:
        while name.startswith('И'):
            name_start_i.append(name)
            break
        while name.startswith('П'):
            name_start_p.append(name)
            break
        while name.startswith('М'):
            name_start_m.append(name)
            break
    my_dict = {
        'И':name_start_i,
        'М':name_start_m,
        'П':name_start_p
    }
    return my_dict


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Маша'))