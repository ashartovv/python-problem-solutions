# Input:
# Continue the program to randomly place ships from the game "Battleship"
# on a game board (a two-dimensional list) named game_board of size N x N.
#
# The following ships must be placed on the board:
# - One four-cell ship.
# - Two three-cell ships.
# - Three two-cell ships.
# - Four one-cell ships.
#
# Each ship can be placed either horizontally or vertically and must not
# extend beyond the boundaries of the board.
# Ships must not touch each other, even diagonally.
#
# The following variables are provided:
# N = 10  # The size of the game board (N x N).
# game_board = [[0] * N for _ in range(N)]
# size_ships = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
#
# A value of 0 in game_board represents an empty cell.
# A value of 1 represents a cell occupied by a ship.
#
# Use the random module to generate random ship positions and orientations:
# import random
# random.randint(a, b) returns a random integer in the inclusive range [a, b].
#
# Your task is to populate game_board by placing all the specified ships.
# Do not print anything to the screen.
#
# Test data:
# Input:
# N = 10
# game_board = [[0] * N for _ in range(N)]
# size_ships = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
#
# Output:
# A randomly generated game_board containing all 10 ships.
# All ships must fit within the board and must not touch each other,
# including diagonally.
# Empty cells must contain 0, and occupied cells must contain 1.
# No output should be printed to the screen.
import random

def is_valid_cell(board, board_index, row, col):
    for row_index in range(-1, 2):
        if row == 0 and row_index == -1 or row == board_index and row_index == 1:
            continue
        for col_index in range(-1, 2):
            if col == 0 and col_index == -1 or col == board_index and col_index == 1:
                continue

            if board[row + row_index][col + col_index]:
                return False
    return True


def get_ship_coords(board, ship):
    board_index = len(board) - 1
    direction = ["right","down"][random.randint(0, 1)]
    if direction == "right":
        row = random.randint(0, board_index)
        col = random.randint(0, board_index - ship + 1)
    else:
        row = random.randint(0, board_index - ship + 1)
        col = random.randint(0, board_index)

    for cell in range(ship):
        if direction == "right":
            if is_valid_cell(board, board_index, row, col+cell) == False:
                return "failed"

        else:
            if is_valid_cell(board, board_index, row+ cell, col) == False:
                return "failed"

    for filling_cell in range(ship):
        if direction == "right":
            board[row][col+filling_cell] = 1

        else:
            board[row+filling_cell][col] = 1

    return board


def fill_ships(game_board, ships):
    board = game_board.copy()
    for ship in ships:
        while True:
            result = get_ship_coords(board, ship)
            if result != "failed" :
                break

    return board


N = 10
size_ships = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
game_board = fill_ships([[0] * N for _ in range(N)], size_ships)