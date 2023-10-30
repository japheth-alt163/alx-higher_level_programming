#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a given position on the board.

    Args:
        board (list of lists): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
"""
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, solutions):
    """
    Solve the N-queens problem using backtracking.

    Args:
        board (list of lists): The current state of the chessboard.
        row (int): The current row to explore.
        solutions (list of lists): List to store the solutions found.

    Returns:
        None
    """
    n = len(board)
    if row == n:
        solutions.append(["[{}, {}]".format(r, c) for r, row in enumerate(board) for c, val in enumerate(row) if val == 1])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1, solutions)
            board[row][col] = 0

def main():
    """
    Main function to handle input, solve the N-queens problem, and print solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)    
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
