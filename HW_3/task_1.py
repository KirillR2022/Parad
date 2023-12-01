def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, player):
    # Проверка строк
    for i in range(0, 9, 3):
        if all(board[j] == player for j in range(i, i + 3)):
            return True

    # Проверка столбцов
    for i in range(3):
        if all(board[j] == player for j in range(i, 9, 3)):
            return True

    # Проверка диагоналей
    if all(board[i] == player for i in range(0, 9, 4)) or all(board[i] == player for i in range(2, 7, 2)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for cell in board)


def game():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)

        move = int(input(f"Игрок {current_player}, выберите ячейку (1-9): ")) - 1

        if 0 <= move < 9 and board[move] == " ":
            board[move] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Неверный ход. Выберите свободную ячейку (1-9).")

if __name__ == "__main__":
    game()
