from sys import stdin


def dp(col, row, test_board):
    for col_idx in range(col - 1):
        for i in range(row):
            for j in [-1, 0, 1]:
                if -1 < i + j < row:
                    test_board[i + j][col_idx + 1] = max(test_board[i + j][col_idx + 1], board[i][col_idx] + board[i + j][col_idx + 1])

        for i in range(row):
            board[i][col_idx + 1] = test_board[i][col_idx + 1]


for _ in range(int(stdin.readline())):
    row, col = map(int, stdin.readline().split())
    board = [[] for k in range(row)]

    data = list(map(int, stdin.readline().split()))
    idx = 0
    for i in range(row):
        for j in range(col):
            board[i].append(data[idx])
            idx += 1
    test_board = [item[:] for item in board]
    dp(col, row, test_board)

    result = -1e9

    for i in range(row):
        result = max(board[i][-1], result)

    print(result)
""" 
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4 
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
