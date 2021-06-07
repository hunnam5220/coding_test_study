from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = []
virus_xy = []

for i in range(n):
    data = list(map(int, stdin.readline().split()))
    board.append(data)
    for j in range(len(data)):
        if data[j] == 2:
            virus_xy.append((i, j))

score = -1e9
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def get_score(board):
    global score
    cnt = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                cnt += 1

    score = max(score, cnt)


def insfection(x, y, board):
    q = deque()
    q.append((x, y))

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    q.append((nx, ny))


def solutions(cnt):
    if cnt == 3:
        new_board = [item[:] for item in board]
        for x, y in virus_xy:
            insfection(x, y, new_board)
        get_score(new_board)

    else:
        for x in range(n):
            for y in range(m):
                if board[x][y] == 0:
                    board[x][y] = 1
                    cnt += 1
                    solutions(cnt)
                    cnt -= 1
                    board[x][y] = 0


solutions(0)
print(score)