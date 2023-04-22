def print_board(board):
    """Prints the tic-tac-toe board."""
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def get_move(player):
    """Prompts the player to enter their move."""
    move = input(f"Player {player}, enter your move (row, col): ")
    row, col = map(int, move.split(","))
    return row, col

def is_winner(board, player):
    """Checks if the player has won."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def play_game():
    """Plays a game of tic-tac-toe."""
    board = [[" ", " ", " "] for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row, col = get_move(player)
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = player
        if is_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("Tie!")
            break
        player = "O" if player == "X" else "X"

play_game()
