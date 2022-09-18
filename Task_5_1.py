"""Напишите программу, удаляющую из текста все слова, содержащие ""абв"""""
st = 'абввкен про7о абвкен, bjnfbb - апиа. абв'

list_str = [i for i in st.split(' ') if 'абв' not in i]

print(' '.join(list_str))

list_str_1 = ' '.join(list(filter(lambda x: 'абв' not in x, st.split(' '))))
print(list_str_1)