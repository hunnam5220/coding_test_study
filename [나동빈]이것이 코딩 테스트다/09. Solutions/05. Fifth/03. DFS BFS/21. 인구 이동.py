from sys import stdin
from collections import deque


n, l, r = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

union = [[-1] * n for _ in range(n)]
dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
union_xy = [[] for _ in range((n * n) + 1)]


def get_union(x, y, union_num):
    q = deque()
    visited.add((x, y))

    q.append((x, y))
    val = board[x][y]
    cnt, flag = 1, False

    union_xy[union_num].append((x, y))

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if -1 < nx < n and -1 < ny < n and (nx, ny) not in visited:
                if l <= abs(board[a][b] - board[nx][ny]) <= r:
                    visited.add((nx, ny))
                    q.append((nx, ny))
                    union[nx][ny] = union_num
                    cnt += 1
                    val += board[nx][ny]
                    union_xy[union_num].append((nx, ny))
                    flag = True

    if not flag:
        union[x][y] = -1
        union_xy[union_num] = []
        val = 0

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
                union[x][y] = union_num
                flag, val = get_union(x, y, union_num)
                if flag:
                    move_tf = True
                    tmp.append((union_num, val))
                    union_num += 1

    if move_tf:
        for t in tmp:
            unum, val = t
            for x, y in union_xy[unum]:
                board[x][y] = val
                union[x][y] = -1
            union_xy[unum] = []

        total_cnt += 1
    else:
        break


print(total_cnt)