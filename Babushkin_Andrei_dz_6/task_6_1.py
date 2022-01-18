with open('nginx_logs.txt', 'r') as file_1:

    for line in file_1:
        for ind in line.split(' '):
            l_t = [line.split(' ')[0], line.split(' ')[5], line.split(' ')[6]]
            l_t[1] = 'GET'
            print(tuple(l_t))