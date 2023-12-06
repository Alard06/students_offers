# Овца и волки

# Импортируем модуль для генерации случайных чисел
import random

# Создаем шахматную доску
board = [['.' for x in range(8)] for y in range(8)]

# Функция для отображения доски
def display_board(board):
    for row in board:
        print(' '.join(row))

# Функция для проверки победы овцы
def check_sheep_win(board):
    for i in range(8):
        if board[0][i] == 'S':
            return True
    return False

# Функция для проверки победы волков
def check_wolf_win(board):
    sheep_pos = []
    wolf_pos = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'S':
                sheep_pos.append((i, j))
            elif board[i][j] == 'W':
                wolf_pos.append((i, j))
    for sheep in sheep_pos:
        for wolf in wolf_pos:
            if abs(sheep[0]-wolf[0]) == 1 and abs(sheep[1]-wolf[1]) == 1:
                return False
    return True

# Расставляем шашки на доске
board[0][1] = 'W'
board[0][3] = 'W'
board[0][5] = 'W'
board[0][7] = 'W'
board[7][4] = 'S'

# Отображаем доску
display_board(board)

# Цикл игры
while True:
    # Ход овцы
    print('Ход овцы')
    while True:
        sheep_row = int(input('Введите строку: '))
        sheep_col = int(input('Введите столбец: '))
        if board[sheep_row][sheep_col] == 'S':
            break
        else:
            print('Вы выбрали неправильную шашку, попробуйте еще раз')
    while True:
        move_row = int(input('Введите строку для хода: '))
        move_col = int(input('Введите столбец для хода: '))
        if abs(sheep_row-move_row) == 1 and abs(sheep_col-move_col) == 1 and board[move_row][move_col] == '.':
            board[sheep_row][sheep_col] = '.'
            board[move_row][move_col] = 'S'
            break
        else:
            print('Вы выбрали неправильный ход, попробуйте еще раз')
    display_board(board)
    if check_sheep_win(board):
        print('Овца выиграла!')
        break
    # Ход волков
    print('Ход волков')
    while True:
        wolf_num = int(input('Выберите волка (1-4): '))
        wolf_row, wolf_col = None, None
        if wolf_num == 1:
            wolf_row, wolf_col = [int(x) for x in input('Введите строку и столбец для первого волка через пробел: ').split()]
        elif wolf_num == 2:
            wolf_row, wolf_col = [int(x) for x in input('Введите строку и столбец для второго волка через пробел: ').split()]
        elif wolf_num == 3:
            wolf_row, wolf_col = [int(x) for x in input('Введите строку и столбец для третьего волка через пробел: ').split()]
        elif wolf_num == 4:
            wolf_row, wolf_col = [int(x) for x in input('Введите строку и столбец для четвертого волка через пробел: ').split()]
        if board[wolf_row][wolf_col] == 'W':
            break
        else:
            print('Вы выбрали неправильную шашку, попробуйте еще раз')
    while True:
        move_row, move_col = None, None
        if sheep_row < wolf_row:
            move_row = wolf_row-1
        else:
            move_row = wolf_row+1
        if sheep_col < wolf_col:
            move_col = wolf_col-1
        else:
            move_col = wolf_col+1
        if board[move_row][move_col] == '.':
            board[wolf_row][wolf_col] = '.'
            board[move_row][move_col] = 'W'
            break
        else:
            print('Вы выбрали неправильный ход, попробуйте еще раз')
    display_board(board)
    if check_wolf_win(board):
        print('Волки выиграли!')
        break