from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def get_union(x, y, index):
    united = [(x, y)]
    q = deque([(x, y)])
    summary = board[x][y]
    count = 1

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    united.append((nx, ny))
                    q.append((nx, ny))
                    union[nx][ny] = index
                    count += 1
                    summary += board[nx][ny]

    for j, k in united:
        board[j][k] = summary // count

    return count


total_cnt = 0


while 1:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for x in range(n):
        for y in range(n):
            if union[x][y] == -1:
                get_union(x, y, index)
                index += 1

    if index == n * n:
        break
    total_cnt += 1

print(total_cnt)