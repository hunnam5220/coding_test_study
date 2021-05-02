from sys import stdin
from collections import deque

n = int(stdin.readline())
board = [[0] * n for _ in range(n)]

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    board[a - 1][b - 1] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solutions():
    x, y = 0, 0
    board[x][y] = 9
    snake = deque()
    snake.append([x, y])
    game_time = 0
    direction = 0
    for _ in range(int(stdin.readline())):
        turn_second, turn_direction = stdin.readline().rstrip().split()
        turn_second = int(turn_second)

        while game_time != turn_second:
            game_time += 1
            x += dx[direction]
            y += dy[direction]

            if x >= n or y >= n or x < 0 or y < 0:
                return game_time

            if board[x][y] == 9:
                return game_time

            snake.append([x, y])

            if board[x][y] == 1:
                board[x][y] = 9
            else:
                board[x][y] = 9
                a, b = snake.popleft()
                board[a][b] = 0

        if turn_direction == "D":
            direction += 1
            if direction > 3:
                direction = 0

        elif turn_direction == "L":
            direction -= 1
            if direction < 0:
                direction = 3

    while board[x][y] != 9 or x < n or y < n or x > 0 or y > 0:
        game_time += 1
        x += dx[direction]
        y += dy[direction]

        if board[x][y] == 9 or x >= n or y >= n or x < 0 or y < 0:
            return game_time

        board[x][y] = 9
        snake.append([x, y])

        if board[x][y] != 1:
            a, b = snake.popleft()
            board[a][b] = 0

    return game_time


print(solutions())