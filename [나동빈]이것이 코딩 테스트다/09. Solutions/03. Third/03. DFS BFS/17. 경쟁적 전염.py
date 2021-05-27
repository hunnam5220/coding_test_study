from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
board = []
virus_data = []

for j in range(n):
    data = list(map(int, stdin.readline().split()))
    board.append(data)
    for i in range(len(data)):
        if data[i] != 0 and (data[i], j, i) not in virus_data:
            virus_data.append((data[i], j, i))

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

s, x, y = map(int, stdin.readline().split())
virus_data.sort()
virus_data = deque(virus_data)


def insfection(vnum, a, b):
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0:
            board[nx][ny] = vnum
            virus_data.append((vnum, nx, ny))


for _ in range(s):
    for _ in range(len(virus_data)):
        vnum, a, b = virus_data.popleft()
        insfection(vnum, a, b)

print(board[x - 1][y - 1])