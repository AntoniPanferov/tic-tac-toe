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

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


# 1 = 0 0; 2 = 0 1; 3 = 0 2
# 4 = 1 0; 5 = 1 1; 6 = 1 2
# 7 = 2 0; 8 = 2 1; 9 = 2 2


def convert_number(number):
    row = (number - 1) // 3
    column = (number - 1) % 3
    print(f"CONVERT NUMBER {row} {column}")

convert_number(9)
def draw_line():
    print("+---+---+---+")

def draw_row(first_number, second_number, third_number):
    print(f"| {first_number} | {second_number} | {third_number} |")

def draw_board():
    draw_line()
    draw_row(board[0][0], board[0][1], board[0][2])
    draw_line()
    draw_row(board[1][0], board[1][1], board[1][2])
    draw_line()
    draw_row(board[2][0], board[2][1], board[2][2])
    draw_line()

def pc_turn():
    print()




draw_board()
