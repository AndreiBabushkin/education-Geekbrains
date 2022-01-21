import os
size_100 = []
size_1000 = []
size_10000 = []
size_100000 = []
for root, dirs, files in os.walk(r'C:/Users/User/Desktop/GeekBrains/dz/Babushkin_Andrei_dz_7'):
    for file in files:
        abs_path = os.path.join(root, file)
        file = os.stat(abs_path)
        if file.st_size < 100:
            size_100.append(file)
        elif file.st_size < 1000 and file.st_size > 100:
            size_1000.append(file)
        elif file.st_size < 10000 and file.st_size > 1000:
            size_10000.append(file)
        elif file.st_size < 100000 and file.st_size > 10000:
            size_100000.append(file)
stat_dict = {
    100: len(size_100),
    1000: len(size_1000),
    10000: len(size_10000),
    100000: len(size_100000)
}
print(stat_dict)