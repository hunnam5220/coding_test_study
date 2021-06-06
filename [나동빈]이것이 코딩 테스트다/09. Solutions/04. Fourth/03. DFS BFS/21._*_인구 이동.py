from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

union_xy = [[] for _ in range((n + 1) * (n + 1))]

dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
union_idx = 0


def bfs(x, y, union_idx, union, visited):
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    val = board[x][y]
    cnt = 1
    flag = False

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                if l <= abs(board[a][b] - board[nx][ny]) <= r:
                    if (a, b) not in union_xy[union_idx]:
                        union_xy[union_idx].append((a, b))

                    if union[nx][ny] == -1:
                        union[nx][ny] = union_idx
                    q.append((nx, ny))
                    visited.add((nx, ny))
                    val += board[nx][ny]
                    union_xy[union_idx].append((nx, ny))
                    cnt += 1
                    flag = True
    if not flag:
        union[x][y] = -1

    return val // cnt, flag


total_move = 0
union = [[-1] * n for _ in range(n)]
while 1:
    union_idx = 0

    # visited 에 중복 제거 처리
    visited = set()
    tmp = []
    move_chk = False

    for x in range(n):
        for y in range(n):
            if (x, y) not in visited:
                union[x][y] = union_idx
                val, flag = bfs(x, y, union_idx, union, visited)
                if flag:
                    move_chk = True
                    tmp.append((union_idx, val))
                    union_idx += 1

    if move_chk:
        for idx, val in tmp:
            for ab in union_xy[idx]:
                x, y = ab
                if union[x][y] == idx:
                    board[x][y] = val
                    union[x][y] = -1

        total_move += 1
    else:
        break

print(total_move)