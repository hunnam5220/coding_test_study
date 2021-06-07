from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())
board = []
union = [[-1] * n for _ in range(n)]
union_xy = [[] for _ in range(n * n + 1)]

for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def get_union(x, y, union_num):
    cnt, flag, val = 1, False, board[x][y]
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    union[x][y] = union_num
    union_xy[union_num].append((x, y))

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(board[a][b] - board[nx][ny]) <= r:
                    visited.add((nx, ny))
                    val += board[nx][ny]
                    q.append((nx, ny))
                    cnt += 1
                    flag = True
                    union[nx][ny] = union_num
                    union_xy[union_num].append((nx, ny))

    if not flag:
        union[x][y] = -1
        union_xy[union_num] = []

    return flag, val // cnt


total_cnt = 0

while 1:
    visited = set()
    union_num = 0
    move_tf = False
    tmp = []

    for x in range(n):
        for y in range(n):
            if (x, y) not in visited:
                flag, val = get_union(x, y, union_num)
                if flag:
                    move_tf = True
                    tmp.append((union_num, val))
                    union_num += 1

    if move_tf:
        for u_num, val in tmp:
            for x, y in union_xy[u_num]:
                board[x][y] = val
                union[x][y] = -1

            union_xy[u_num] = []

        total_cnt += 1
    else:
        break

print(total_cnt)

