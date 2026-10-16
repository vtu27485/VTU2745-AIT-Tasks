def minimax(board, depth, alpha, beta, maximizing):
    if "XXX" in lines(board):
        return 10 - depth
    if "OOO" in lines(board):
        return depth - 10
    if " " not in board:
        return 0

    if maximizing:
        best = -1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, alpha, beta, False)
                board[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, alpha, beta, True)
                board[i] = " "
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


def lines(b):
    return [
        b[0] + b[1] + b[2],
        b[3] + b[4] + b[5],
        b[6] + b[7] + b[8],
        b[0] + b[3] + b[6],
        b[1] + b[4] + b[7],
        b[2] + b[5] + b[8],
        b[0] + b[4] + b[8],
        b[2] + b[4] + b[6]
    ]


board = [
    "X", "O", "X",
    "X", "O", " ",
    " ", " ", " "
]

best_score = -1000
best_move = -1

for i in range(9):
    if board[i] == " ":
        board[i] = "X"
        score = minimax(board, 0, -1000, 1000, False)
        board[i] = " "

        if score > best_score:
            best_score = score
            best_move = i + 1

print("Best move:", best_move)


"""
INPUT:
X O X
X O -
- - -

OUTPUT:
Best move: 8
"""
