# Создайте программу для игры в "Крестики-нолики"

global count
global board
global actual_symbol
board = list(range(1, 10))


def print_board():
    x = ""
    for i in range(3):
        x += str(board[0 + i * 3]) + "|" + str(board[1 + i * 3]) + "|" + str(board[2 + i * 3]) + "\n"
    return x


def start_game():
    global count
    global board
    count = 0
    board = list(range(1, 10))


def take_input(symbol):
    global board
    global actual_symbol
    global count
    if 1 <= symbol <= 9:
        if str(board[symbol - 1]) not in "XO":
            board[symbol - 1] = actual_symbol
            count += 1
            temp = check_win(board)
            if temp:
                count = 0
                return "Ты выиграл!"
            return "1"
        else:
            return "Клетка занята"
    else:
        return "Некорректный ввод. Введите число от 1 до 9."


def check_win(board_work):
    win_coord = ((0, 1, 2),
                 (3, 4, 5),
                 (6, 7, 8),
                 (0, 3, 6),
                 (1, 4, 7),
                 (2, 5, 8),
                 (0, 4, 8),
                 (2, 4, 6))
    for symbol in win_coord:
        if board_work[symbol[0]] == board_work[symbol[1]] == board_work[symbol[2]]:
            return board_work[symbol[0]]
    return False


def next_stape():
    global count
    global actual_symbol
    if count % 2 == 0:
        actual_symbol = "X"
        return "Введите куда ставить Х (от 1 до 9)"
    else:
        actual_symbol = "O"
        return "Введите куда ставить O (от 1 до 9)"


def method_name():
    global win_flag
    board = list(range(1, 10))
    count = 0

    win_flag = False
    if not win_flag:

        count += 1
        if check_win(board):
            print(check_win(board), "выиграл!")
            win_flag = True

        if count == 9:
            print("Ничья!")
