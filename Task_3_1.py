"""В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""
list_1 = []
for i in range(2, 100):
    list_1.append(i)

list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
list_8 = []
list_9 = []


for n in list_1:
    if n % 2 == 0:
        list_2.append(n)
    if n % 3 == 0:
        list_3.append(n)
    if n % 4 == 0:
        list_4.append(n)
    if n % 5 == 0:
        list_5.append(n)
    if n % 6 == 0:
        list_6.append(n)
    if n % 7 == 0:
        list_7.append(n)
    if n % 8 == 0:
        list_8.append(n)
    if n % 9 == 0:
        list_9.append(n)
print(f'Кратны 2: {len(list_2)}')
print(f'Кратны 3: {len(list_3)}')
print(f'Кратны 4: {len(list_4)}')
print(f'Кратны 5: {len(list_5)}')
print(f'Кратны 6: {len(list_6)}')
print(f'Кратны 7: {len(list_7)}')
print(f'Кратны 8: {len(list_8)}')
print(f'Кратны 9: {len(list_9)}')