from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = []
virus_xy = []
max_score = -1e9

for i in range(n):
    data = list(map(int, stdin.readline().split()))
    board.append(data)
    for j in range(m):
        if data[j] == 2:
            virus_xy.append((i, j))


def insfection(board):
    for loc in virus_xy:
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        q = deque()
        q.append(loc)

        while q:
            a, b = q.popleft()
            for i in range(4):
                nx, ny = dx[i] + a, dy[i] + b
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 0:
                        board[nx][ny] = 2
                        q.append((nx, ny))

    return get_score(board)


def get_score(board):
    score = 0
    for data in board:
        for fine in data:
            if fine == 0:
                score += 1
    return score


def function(cnt):
    global max_score
    if cnt == 3:
        test_board = [item[:] for item in board]
        score = insfection(test_board)
        max_score = max(score, max_score)

    else:
        for x in range(n):
            for y in range(m):
                if board[x][y] == 0:
                    board[x][y] = 1
                    cnt += 1
                    function(cnt)
                    cnt -= 1
                    board[x][y] = 0


function(0)
print(max_score)
