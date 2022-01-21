import os
import shutil

copied = []

for root, dirs, files in os.walk('my_project_1'):
    for file in files:
        if file.endswith('.html') and root not in copied:
            dir_name = root.rsplit('\\', 1)[1]
            copied.append(root)
            path = '\\'.join((os.path.abspath(root)).split('\\'))

            try:
                shutil.copytree(path, 'my_project_1/templates/' + dir_name)
            except FileExistsError as e:
                print(e)
