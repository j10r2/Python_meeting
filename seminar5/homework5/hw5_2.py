'''
Создайте программу для игры в "Крестики-нолики"
1. реализовать проверку хода
2. реализовать проверку ввода
'''

def input_check(field_status):
    while True:
        print('куда ставим?')
        try:
            pos = int(input())
            if pos > 0 and pos < 10:
                if field_status[positions[pos - 1][1]][positions[pos - 1][2]] != 'O' \
                        and field_status[positions[pos - 1][1]][positions[pos - 1][2]] != 'X':
                    return pos
                else:
                    print('поле уже занято, выберите другое')
            else:
                print('введите цифру от 1 до 9')
        except:
            print('РОДИНА ОПАСНОСТЕ!!! \n товарищ, нам нужна цифра от 1 до 9')
def rewrite_field(pole, act_field):
    pole = f'+___ ___ ___+ ' \
            f'\n| {act_field[0][0]} | {act_field[0][1]} | {act_field[0][2]} |' \
            '\n+--- --- ---+' \
            f'\n| {act_field[1][0]} | {act_field[1][1]} | {act_field[1][2]} |' \
            '\n+--- --- ---+' \
            f'\n| {act_field[2][0]} | {act_field[2][1]} | {act_field[2][2]} |' \
            '\n+--- --- ---+'
    return pole
def win_check(win_combinations, player_moves):
    for i in range(len(win_combinations)):
        if win_combinations[i][0] in player_moves \
                and win_combinations[i][1] in player_moves \
                and win_combinations[i][2] in player_moves:
            return 'победа'

positions = [(1, 0, 0), (2, 0, 1), (3, 0, 2), (4, 1, 0), (5, 1, 1), (6, 1, 2), (7, 2, 0), (8, 2, 1), (9, 2, 2)]
wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]]
actual_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
field = f'+___ ___ ___+ ' \
            f'\n| {actual_field[2][0]} | {actual_field[2][1]} | {actual_field[2][2]} |' \
            '\n+--- --- ---+' \
            f'\n| {actual_field[1][0]} | {actual_field[1][1]} | {actual_field[1][2]} |' \
            '\n+--- --- ---+' \
            f'\n| {actual_field[0][0]} | {actual_field[0][1]} | {actual_field[0][2]} |' \
            '\n+--- --- ---+'

player_1 = input('введите имя первого игрока: ')
player_2 = input('введите имя второго игрока: ')
players = [(0, player_1, 'X'), (1, player_2, 'O')]
steps = [[], []]
for i in range(9):
    player = players[i % 2][1]
    print(f'ходит {player} \n', rewrite_field(field, actual_field))
    step = input_check(actual_field)
    steps[i % 2].append(step)
    if i >= 4:
        if win_check(wins, steps[i % 2]) == 'победа':
            print(f'победа игрока {player}!\n', rewrite_field(field, actual_field))

            break
    actual_field[positions[step - 1][1]][positions[step - 1][2]] = players[i % 2][2]
    if i == 8:
        print('Ничья...')