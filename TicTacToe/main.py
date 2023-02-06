import os
from art import logo

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
start_board = [row1, row2, row3]


def draw_board(current_board):
    print(current_board[0][0] + "|" + current_board[0][1] + "|" + current_board[0][2])
    print("------")
    print(current_board[1][0] + "|" + current_board[1][1] + "|" + current_board[1][2])
    print("------")
    print(current_board[2][0] + "|" + current_board[2][1] + "|" + current_board[2][2])
    print()


def update_board(r, c, turn, board):
    board[r-1][c-1] = turn
    return board


def position_check(board):
    # Check that inputted row and column are valid numbers
    while True:
        while True:
            row = input("Please enter a row: ")
            if not row.isdigit():
                print("Incorrect entry. Please enter a number.")
            else:
                row = int(row)
                if 0 < row < 4:
                    break
                else:
                    print("Incorrect entry. Number must be 1, 2 or 3.")

        while True:
            column = input("Please enter a column: ")
            if not column.isdigit():
                print("Incorrect entry. Please enter a number.")
            else:
                column = int(column)
                if 0 < column < 4:
                    break
                else:
                    print("Incorrect entry. Number must be 1, 2 or 3.")

        if board[row-1][column-1] == " ":
            break

    return row, column


def choose_players():
    player1 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input("Player 1 choose 'X' or 'O': ")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1, player2


def display_winner(winning_player):
    print(f"Player {winning_player} wins!")
    print("Thanks for playing!")


def check_winner(board, player):
    if (board[0][0] == board[0][1] == board[0][2] == player) or (board[1][0] == board[1][1] == board[1][2] == player) or (board[2][0] == board[2][1] == board[2][2] == player):
        display_winner(player)
        return False
    elif (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        display_winner(player)
        return False
    elif (board[0][0] == board[1][0] == board[2][0] == player) or (board[0][1] == board[1][1] == board[2][1] == player) or (board[0][2] == board[1][2] == board[2][2] == player):
        display_winner(player)
        return False
    else:
        return True


def tic_tac_toe():
    print(logo)
    print("Welcome to Tic Tac Toe!\n")
    game_board = start_board
    draw_board(game_board)
    (player1, player2) = choose_players()
    i = 0
    game_over = True
    while game_over:
        if i % 2 == 0:
            print("*** Player 1 Turn ***")
            (row, column) = position_check(game_board)
            game_board = update_board(row, column, player1, game_board)
            os.system('cls' if os.name == 'nt' else 'clear')
            draw_board(game_board)
            game_over = check_winner(game_board, player1)
            i = i + 1
        else:
            print("*** Player 2 Turn ***")
            (row, column) = position_check(game_board)
            game_board = update_board(row, column, player2, game_board)
            os.system('cls' if os.name == 'nt' else 'clear')
            draw_board(game_board)
            game_over = check_winner(game_board, player2)
            i = i + 1


tic_tac_toe()