from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
board = []
virus_xy = []
idx = len(virus_xy)

for i in range(n):
    data = list(map(int, stdin.readline().split()))
    board.append(data)
    for j in range(n):
        if data[j] != 0 and data[j] not in virus_xy:
            virus_xy.append((data[j], i, j))

virus_xy.sort()

s, x, y = map(int, stdin.readline().split())
q = deque()
q.extend(virus_xy)
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def insfection(vnum, a, b):
    for j in range(4):
        nx, ny = a + dx[j], b + dy[j]
        if -1 < nx < n and -1 < ny < n and board[nx][ny] == 0:
            q.append((vnum, nx, ny))
            board[nx][ny] = vnum


for _ in range(s):
    virus_xy = list(q)
    for _ in virus_xy:
        v, a, b = q.popleft()
        insfection(v, a, b)

print(board[x-1][y-1])

