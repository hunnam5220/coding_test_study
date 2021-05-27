from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
board = []
virus = []
zero_cnt = 0


for p in range(n):
    data = list(map(int, stdin.readline().split()))
    board.append(data)


for i in range(len(data)):
    if data[i] != 0 and i not in virus:
        virus.append((data[i], p, i))
    else:
        zero_cnt += 1

virus.sort()
virus = deque(virus)
v_len = len(virus)

s, x, y = map(int, stdin.readline().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def insfection(vir, n):
    virus_num, nx, ny = vir
    for i in range(4):
        tx = nx + dx[i]
        ty = ny + dy[i]
        if (0 <= tx < n) and (0 <= ty < n):
            if board[tx][ty] == 0:
                board[tx][ty] = virus_num
                virus.append((virus_num, tx, ty))


for l in range(s):
    cnt = 0
    while cnt != v_len and virus:
        v_data = virus.popleft()
        insfection(v_data, n)
        cnt += 1

print(board[x - 1][y - 1])