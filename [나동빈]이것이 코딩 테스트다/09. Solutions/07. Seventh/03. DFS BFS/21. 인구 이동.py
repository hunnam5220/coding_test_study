from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

union = [[-1] * n for _ in range(n)]
union_xy = [[] for _ in range(n * n + 1)]
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def solution(x, y, union_num):
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    union_xy[union_num].append((x, y))
    union[x][y] = union_num
    flag, val, cnt = False, board[x][y], 1

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if -1 < nx < n and -1 < ny < n and (nx, ny) not in visited:
                if l <= abs(board[a][b] - board[nx][ny]) <= r:
                    visited.add((nx, ny))
                    q.append((nx, ny))
                    val += board[nx][ny]
                    union[nx][ny] = union_num
                    union_xy[union_num].append((nx, ny))
                    cnt += 1
                    flag = True

    if not flag:
        union_xy[union_num] = []
        union[x][y] = -1

    return flag, val // cnt


total_cnt = 0
while 1:
    visited = set()
    union_num = 0
    move_tf, tmp = False, []

    for x in range(n):
        for y in range(n):
            if (x, y) not in visited:
                flag, val = solution(x, y, union_num)
                if flag:
                    move_tf = True
                    tmp.append((val, union_num))
                    union_num += 1

    if move_tf:
        for val, un_num in tmp:
            for x, y in union_xy[un_num]:
                board[x][y] = val
                union[x][y] = -1
            union_xy[un_num] = []

        total_cnt += 1
    else:
        break


print(total_cnt)