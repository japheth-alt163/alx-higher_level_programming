#!/usr/bin/python3
"""Solves the N-queens puzzle"""


import sys

# Initialize an NxN chessboard with empty spaces


def init_board(n):
    board = []
    for _ in range(n):
        row = [' '] * n
        board.append(row)
    return board


# Create a deep copy of the chessboard
def board_deepcopy(board):
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


# Get the solution as a list of queen positions [row, column]
def get_solution(board):
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


# Mark non-attacking positions on the board as 'x' after placing a queen
def xout(board, row, col):
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1


# Recursively solve the N-queens puzzle
def recursive_solve(board, row, queens, solutions):
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    # Check and validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard and find solutions
    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])

    # Print the solutions
    for sol in solutions:
        print(sol)
