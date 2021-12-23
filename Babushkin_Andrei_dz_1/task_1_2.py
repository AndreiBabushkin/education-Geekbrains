lst_kube = []

for i in range(1, 1000, 2):
    lst_kube.append(i ** 3 + 17)

sum_lst = 0

for idx in lst_kube:
    a = 0
    while idx != 0:
        a += idx % 10
        idx = idx // 10
    if a % 7 == 0:
        sum_lst += a
print(sum_lst)