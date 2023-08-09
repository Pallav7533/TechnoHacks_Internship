import random

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']

def get_computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        if current_player == 'X':
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        else:
            print(f"Computer (O) is making a move...")
            row, col = get_computer_move(board)
        
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

play_tic_tac_toe()
