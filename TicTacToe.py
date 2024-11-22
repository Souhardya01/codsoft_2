import math
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "
def create_board():
    """Create a new Tic-Tac-Toe board."""
    return [EMPTY for _ in range(9)]
def print_board(board):
    """Print the current state of the board."""
    print("\n")
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("--+---+--")
    print("\n")
def winner(board, player):
    """Check if the specified player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)
def is_draw(board):
    """Check if the game is a draw."""
    return EMPTY not in board
def minimax(board, depth, is_maximizing, alpha, beta):
    """Minimax algorithm with alpha-beta pruning."""
    if winner(board, PLAYER_O):  # AI's win
        return 10 - depth
    if winner(board, PLAYER_X):  # User's win
        return depth - 10
    if is_draw(board):  # Draw
        return 0
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
def best_move(board):
    """Determine the best move for the AI."""
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_O
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY
            if move_val > best_val:
                best_val = move_val
                move = i
    return move
def play_game():
    """Main function to play the Tic-Tac-Toe game."""
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the AI is O. Make your move by entering a number (1-9):")
    print_board(board)
    while True:
        while True:
            try:
                human_move = int(input("Your move (1-9): ")) - 1
                if human_move < 0 or human_move > 8 or board[human_move] != EMPTY:
                    print("Invalid move! Please enter a number between 1 and 9 that is not already taken.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
        board[human_move] = PLAYER_X
        print_board(board)

        if winner(board, PLAYER_X):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break       
        print("AI is making its move...")
        ai_move = best_move(board)
        board[ai_move] = PLAYER_O
        print_board(board)
        if winner(board, PLAYER_O):
            print("AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()