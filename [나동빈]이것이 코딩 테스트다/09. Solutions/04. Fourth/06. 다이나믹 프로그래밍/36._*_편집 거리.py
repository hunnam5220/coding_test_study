from sys import stdin


def sol(s1, s2):
    n = len(s1)
    m = len(s2)

    board = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        board[i][0] = i

    for i in range(1, m + 1):
        board[0][i] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                board[i][j] = board[i - 1][j - 1]
            else:
                board[i][j] = 1 + min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1])

    return board[n][m]


print(sol(stdin.readline().rstrip(), stdin.readline().rstrip()))

"""
saturday
sunday
"""