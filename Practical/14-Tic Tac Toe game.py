# Tic Tac Toe Game in Python

# Function to print board
def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Function to check for win
def check_winner(board, player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8], 
        [0,4,8], [2,4,6]           
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def check_draw(board):
    return all(cell != " " for cell in board)


def play_game():
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        try:
            move = int(input(f"Player {current_player}, choose your position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid position! Choose between 1-9.")
                continue
            if board[move] != " ":
                print("Position already taken! Try again.")
                continue
            
            board[move] = current_player
            print_board(board)
            
            if check_winner(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break
            if check_draw(board):
                print("It's a draw!")
                break
            
            # Switch player
            current_player = "O" if current_player == "X" else "X"
        
        except ValueError:
            print("Please enter a valid number!")


play_game()
