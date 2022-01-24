def type_logger(func):
    def logger(*args, **kwargs):
        list_int = []
        for i in args:
            list_int.append((f'{func.__name__}({i}: {type(i)})'))
        return ', '.join(list_int)


    return logger


@type_logger
def calc_cube(x):
    return x**3

a = calc_cube(8, 9, 2.5, -8, 'integer')
print(a)




