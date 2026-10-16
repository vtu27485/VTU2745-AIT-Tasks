def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nq(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nq(board, col + 1, n):
                return True

            board[row][col] = 0

    return False


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_nq(board, 0, n):
        print(f"Solution for {n}-Queen problem:")
        for row in board:
            print(" ".join("Q" if x == 1 else "-"
                           for x in row))
    else:
        print("Solution does not exist")


n = int(input("Enter the value of N: "))
solve_n_queens(n)


"""
INPUT:
Enter the value of N: 4

OUTPUT:
Solution for 4-Queen problem:
- - Q -
Q - - -
- - - Q
- Q - -
"""
