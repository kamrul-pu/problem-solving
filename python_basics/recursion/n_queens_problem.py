# """Place N-Queens using Recursion."""
import copy


def is_safe(row: int, col: int, board: list[str], n: int) -> bool:
    duprow: int = row
    dupcol: int = col
    # check upper diagonal
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    col = dupcol
    row = duprow
    # check left columns
    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1

    row = duprow
    col = dupcol
    # check lower diagonal
    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False
        row += 1
        col -= 1

    return True


def solve(col: int, board: list[str], ans: list[list[int]], n: int) -> None:
    if col == n:
        ans.append(copy.deepcopy(board))
        return

    for row in range(n):
        if is_safe(row=row, col=col, board=board, n=n):
            board[row][col] = "Q"
            solve(col=col + 1, board=board, ans=ans, n=n)
            board[row][col] = "."


if __name__ == "__main__":
    # n: int = int(input())
    n: int = 4
    ans: list[list[str]] = []
    board: list[list[str]] = [["." for col in range(n)] for _ in range(n)]
    print(board)
    solve(col=0, board=board, ans=ans, n=n)
    print(ans)


# def is_safe(board, row, col, n):
#     # Check if there is a queen in the same column
#     for i in range(row):
#         if board[i][col] == 1:
#             return False

#     # Check if there is a queen in the left diagonal
#     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     # Check if there is a queen in the right diagonal
#     for i, j in zip(range(row, -1, -1), range(col, n)):
#         if board[i][j] == 1:
#             return False

#     return True


# def solve_nqueens_util(board, row, n, solutions):
#     if row == n:
#         solutions.append([list(row) for row in board])
#         return

#     for col in range(n):
#         if is_safe(board, row, col, n):
#             board[row][col] = 1
#             solve_nqueens_util(board, row + 1, n, solutions)
#             board[row][col] = 0  # Backtrack


# def solve_nqueens(n):
#     board = [[0 for _ in range(n)] for _ in range(n)]
#     solutions = []
#     solve_nqueens_util(board, 0, n, solutions)
#     return solutions


# # Example: Solve N-Queens for N = 4
# n = 4
# solutions = solve_nqueens(n)

# # Print the solutions
# for i, solution in enumerate(solutions):
#     print(f"Solution {i+1}:")
#     for row in solution:
#         print(row)
#     print()
