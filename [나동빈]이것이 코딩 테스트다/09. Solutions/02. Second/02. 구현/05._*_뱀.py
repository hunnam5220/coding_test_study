from sys import stdin
from collections import deque

# 시간 증가는 코드 후반에
direction = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n, k = int(stdin.readline().rstrip()), int(stdin.readline().rstrip())
board = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    board[a - 1][b - 1] = 1


def turn_head(direction, c):
    if direction < 3 and c == "D":
        return direction + 1

    elif 0 < direction and c == "L":
        return direction - 1

    elif direction == 3 and c == "D":
        return 0

    elif direction == 0 and c == "L":
        return 3


def solutions(direction):
    x, y = 0, 0
    snake = deque([(x, y)])
    board[x][y] = 9
    t = 0
    for _ in range(int(stdin.readline().rstrip())):
        a, c = stdin.readline().split()
        a = int(a)

        while a != t:
            x += dx[direction]
            y += dy[direction]

            if x < 0 or y < 0 or x >= n or y >= n or board[x][y] == 9:
                return t + 1

            snake.append((x, y))

            if board[x][y] != 1:
                x1, y1 = snake.popleft()
                board[x1][y1] = 0
                board[x][y] = 9
            else:
                board[x][y] = 9

            t += 1

            if t == a:
                direction = turn_head(direction, c)

    while True:
        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= n or y >= n or board[x][y] == 9:
            return t + 1

        snake.append((x, y))

        if board[x][y] != 1:
            x1, y1 = snake.popleft()
            board[x1][y1] = 0
            board[x][y] = 9
        else:
            board[x][y] = 9

        t += 1


print(solutions(direction))
