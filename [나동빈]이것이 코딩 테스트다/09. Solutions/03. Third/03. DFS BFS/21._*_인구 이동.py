from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def get_union(x, y):
    flag = False
    visited = {(x, y)}
    q = deque([])
    q.append((x, y))
    cnt, val = 0, 0

    while q:
        a, b = q.popleft()
        val += board[x][y]
        cnt += 1
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i] 

            if 0 <= nx < len(board) and 0 <= ny < len(board) and (nx, ny) not in visited and l <= abs(board[nx][ny] - board[a][b]) <= r:
                q.append((nx, ny))
                visited.add((nx, ny))
                flag = True

    return val // cnt, visited, flag


total_count = 0
cnt = 0
while 1:
    is_move = False

    total_visited = set()
    temp = []

    for i in range(n):
        for j in range(n):
            if (i, j) not in total_visited:
                value, visited, flag = get_union(i, j)
                if flag:
                    is_move = True
                temp.append((value, visited))
                total_visited |= visited

    for (value, visit) in temp:
        for x, y in visit:
            board[x][y] = value

    if not is_move:
        print(cnt)
        break
    cnt += 1

print(total_count)
