# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
def input_check(sum):
    while True:
        if sum <= 28:
            max = sum
        else:
            max = 28
        print(f'сколько конфет берём? (максимум {max})')
        try:
            pos = int(input())
            if pos > 0 and pos <= 28:
                    return pos
            else:
                print('попробуй ещё раз')
        except:
            print('Мы в конфетки играем. Пиши цифру или уходи')

player_1 = input('введите имя первого игрока: ')
player_2 = input('введите имя второго игрока: ')
players = [(0, player_1), (1, player_2)]
number = int(input('на сколько конфет играем?'))
first = random.randint(0, 1)
while number > 0:
    print(f'ходит {players[first%2][1]}')
    number -= input_check(number)
    if number == 0:
        print(f'{players[first%2][1]} побеждает и забирает себе все конфеты! \n {players[first%2-1][1]} остётся ни с чем')
        break
    first = first % 2 + 1
    print(number)
