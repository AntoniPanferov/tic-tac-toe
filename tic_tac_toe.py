# Your task is to write a simple program which pretends to play tic-tac-toe with the user. To
# make it all easier for you, we've decided to simplify the game. Here are our assumptions:
# • the computer (i.e., your program) should play the game using 'X's;
# • the user (e.g., you) should play the game using 'O's;
# • the first move belongs to the computer - it always puts its first 'X' in the middle of the board;
# • all the squares are numbered row by row starting with 1 (see the example session below for reference)
# • the user inputs their move by entering the number of the square they choose - the number
#   must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it
#   cannot point to a field which is already occupied;
# • the program checks if the game is over - there are four possible verdicts: the game should
#   continue, or the game ends with a tie, your win, or the computer's win;
# • the computer responds with its move and the check is repeated;
# • don't implement any form of artificial intelligence - a random field choice made by the
#   computer is good enough for the game.

# Implement the following features:
# • the board should be stored as a three-element list, while each element is another three-element list
#   (the inner lists represent rows) so that all the squares may be accessed using the following syntax:
#   board[row][column]
# • each of the inner list's elements can contain 'O', 'X', or a digit representing the square's
#   number (such a square is considered free)
# • the board's appearance should be exactly the same as the one presented in the example.
# • implement the functions defined for you in the editor.

# 1 2 3
# 4 5 6
# 7 8 9
# Win conditions: 123, 456, 789, 147, 258, 369, 159, 357

import random


def print_board(board):
    print("+---+---+---+")
    for row in board:
        print("|", end=" ")
        print(" | ".join(row), end=" ")
        print("|")
        print("+---+---+---+")


def check_winner(board, player):
    for row in board + list(zip(*board)):
        if row.count(player) == 3:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell not in ["o", "x"]:
                return False
    return True


def is_valid_move(board, move):
    if 1 <= move <= 9:
        row = (move - 1) // 3
        col = (move - 1) % 3
        return board[row][col] == str(move)
    return False


def user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if is_valid_move(board, move):
                return move
            else:
                print("Invalid move. Please choose a free tile.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def computer_move(board):
    while True:
        move = random.randint(1, 9)
        if is_valid_move(board, move):
            return move


def start_game():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    print_board(board)

    for _ in range(4):
        user_input = user_move(board)
        row, col = (user_input - 1) // 3, (user_input - 1) % 3
        board[row][col] = "o"

        if check_winner(board, "o"):
            print_board(board)
            print("Congratulations! You win!")
            return

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            return

        print_board(board)

        computer_input = computer_move(board)
        row, col = (computer_input - 1) // 3, (computer_input - 1) % 3
        print("Computer´s turn")
        board[row][col] = "x"

        if check_winner(board, "x"):
            print_board(board)
            print("You lose.")
            return

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            return

        print_board(board)


start_game()
