"""Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом"""""
import random


table = 60


def move_player():

    while True:
        move = int(input('Делайте ход (можно забрать не более чем 28 конфет): '))
        if move > 28:
            print('Такой ход запрещен')
        else:
            return move


player = True
first_move = random.randint(1, 2)
if first_move == 1:
    player = True
    print('Ходит первый игрок')
else:
    player = False
    print('Ходит бот')
while table != 0:
    if player is True:
        table -= move_player()
        print(f'На столе осталось {table} конфет')
        player = False
    elif player is False:
        if 56 > table >= 29:
            move_bot = random.randint(1, table - 28)
            print(f'Бот взял {move_bot} конфет')
            table -= move_bot
            print(f'На столе осталось {table} конфет')
            player = True
        else:
            move_bot = random.randint(1, 29)
            print(f'Бот взял {move_bot} конфет')
            table -= move_bot
            print(f'На столе осталось {table} конфет')
            player = True
    if table <= 28:
        if player is True:
            print('Победил первый игрок')
            break
        else:
            print('Победил бот')
            break
