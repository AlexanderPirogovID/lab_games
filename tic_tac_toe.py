def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"ход игрока {current_player}. введите координаты строки и столбца через пробел (от 0 до 2):")

        try:
            row, col = map(int, input().split())
        except ValueError:
            print("ошибка ввода, введите две цифры через пробел")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("координаты должны быть от 0 до 2")
            continue

        if board[row][col] != ' ':
            print("эта клетка уже занята")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"игрок {current_player} выиграл")
            break

        if is_draw(board):
            print_board(board)
            print("ничья")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()