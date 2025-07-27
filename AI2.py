def show_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(b, player):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] == player:
            return True
        if b[0][i] == b[1][i] == b[2][i] == player:
            return True
    if b[0][0] == b[1][1] == b[2][2] == player:
        return True
    if b[0][2] == b[1][1] == b[2][0] == player:
        return True
    return False

def board_full(b):
    for row in b:
        if " " in row:
            return False
    return True

def empty_positions(b):
    positions = []
    for i in range(3):
        for j in range(3):
            if b[i][j] == " ":
                positions.append((i, j))
    return positions

def minimax(b, turn):
    if check_winner(b, "O"):
        return 1
    elif check_winner(b, "X"):
        return -1
    elif board_full(b):
        return 0

    if turn == "O":
        best = -100
        for i, j in empty_positions(b):
            b[i][j] = "O"
            score = minimax(b, "X")
            b[i][j] = " "
            if score > best:
                best = score
        return best
    else:
        best = 100
        for i, j in empty_positions(b):
            b[i][j] = "X"
            score = minimax(b, "O")
            b[i][j] = " "
            if score < best:
                best = score
        return best

def best_ai_move(b):
    move = None
    max_score = -100
    for i, j in empty_positions(b):
        b[i][j] = "O"
        score = minimax(b, "X")
        b[i][j] = " "
        if score > max_score:
            max_score = score
            move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome! You are X, AI is O.")
    show_board(board)

    while True:
        # Player move
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("That spot is taken.")
            except:
                print("Please enter valid row and column numbers.")
        show_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if board_full(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_row, ai_col = best_ai_move(board)
        if ai_row is not None:
            board[ai_row][ai_col] = "O"
        show_board(board)

        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break
        if board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()