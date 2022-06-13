"""Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке."""
import random
import hashlib


N = 10
list_1 = [random.randint(97, 122) for _ in range(N)]
list_1 = [chr(i) for i in list_1]
S = ''.join(list_1)

sum_set = set()

for num in range(len(S)):
    for j in range(len(S), num, -1):
        hash_str = hashlib.sha1(S[num:j].encode('utf-8')).hexdigest()
        sum_set.add(hash_str)
print(f'{len(sum_set) - 1} количество подстрок в строке {S}')


