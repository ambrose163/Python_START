# Напишите игру "Крестики-нолики".


print('Крестики-нолики')

board = list(range(1, 10))


def draw_board(board):
    print('-' * 10)
    for i in range(3):
        print(board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3])
        print('-' * 10)


def make_move(cone):
    flag = False
    while not flag:
        answer = input('Куда ставим ' + cone + '? Введите число от 1 до 9: ')

        try:
            answer = int(answer)
        except:
            print('Введите число от 1 до 9: ')
            continue

        if answer >=1 and answer <= 9:
            if str(board[answer - 1]) not in 'X0':
                board[answer - 1] = cone
                flag = True
            else:
                print('Клетка занята')
        else:
            print('Введите число от 1 до 9: ')


def check_win(board):
    win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_combo:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            make_move('X')
        else:
            make_move('0')
        count += 1

        if count > 4:
            check = check_win(board)
            if check:
                print('Ура, это победа!')
                win = True
                break
        if count == 9:
            print('Это ничья!')
            break
    draw_board(board)


main(board)