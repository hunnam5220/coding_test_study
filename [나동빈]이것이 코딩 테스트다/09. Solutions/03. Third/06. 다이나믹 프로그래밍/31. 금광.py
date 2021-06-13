from sys import stdin


for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    board = []
    data = list(map(int, stdin.readline().split()))
    for i in range(n):
        board.append(data[i * m: (i + 1) * m])

    result = 0

    test_board = [item[:] for item in board]
    for i in range(1, m):
        for j in range(n):
            for k in [-1, 0, 1]:
                if n > j + k >= 0:
                    test_board[j][i] = max(board[j + k][i - 1] + board[j][i], test_board[j][i])

        for p in range(n):
            board[p][i] = test_board[p][i]
            result = max(max(board[p]), result)

    print(result)

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""