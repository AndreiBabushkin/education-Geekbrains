import os

def make_names_dirs_in_my_project(*args):
    for name in args:
        if name.find('.') == - 1:
            make_dirs = os.path.join('my_project', name)
            if not os.path.exists(make_dirs):
                os.makedirs(make_dirs)
        elif name.find('.') > - 1:
            file = open(name, 'x')
            file.close()
            os.replace(name, 'my_project/' + name)


make_names_dirs_in_my_project('settings', 'mainapp', 'adminapp', 'authapp', 'file.txt', 'file_2.txt')