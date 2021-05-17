from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
board = [[0] * n for _ in range(n)]

for step in range(int(stdin.readline().rstrip())):
    a,b = map(int, stdin.readline().rstrip().split())
    board[a - 1][b - 1] = 1

direction = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
board[x][y] = 9
snake = deque([(x, y)])


def solution(x, y, n, direction):
    game_time = 0

    for _ in range(int(stdin.readline().rstrip())):
        turn_time, direct = stdin.readline().split()
        turn_time = int(turn_time)

        while turn_time != game_time:
            game_time += 1

            x += dx[direction]
            y += dy[direction]

            if x < 0 or y < 0 or x >= n or y >= n:
                return game_time

            if board[x][y] == 1:
                board[x][y] = 9
                snake.append((x, y))

            elif board[x][y] == 9:
                return game_time

            else:
                board[x][y] = 9
                snake.append((x, y))
                hx, hy = snake.popleft()
                board[hx][hy] = 0

        if direct == 'D':
            direction += 1

        elif direct == 'L':
            direction -= 1

        if direction > 3:
            direction = 0

        elif direction < 0:
            direction = 3

    while not (x < 0 or y < 0 or x >= n or y >= n):
        game_time += 1

        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= n or y >= n:
            return game_time

        if board[x][y] == 1:
            board[x][y] = 9

        elif board[x][y] == 9:
            return game_time

        else:
            board[x][y] = 9
            snake.append((x, y))
            hx, hy = snake.popleft()
            board[hx][hy] = 0

    return game_time


print(solution(x, y, n, direction))
"""
# 9
6
3
3 4
2 5
5 3
5 3
3
3 D
15 L
17 D

# 21
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

# 13
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

# 20
5
0
5
4 D
8 D
12 D
15 D
20 L

# 21
8
3
5 4
5 8
2 5
6
7 D
11 D
15 D
18 D
19 D
20 D

# 27
8
5
6 1
7 3
3 5
5 7
5 6
12
2 D
8 D
10 D
12 D
18 L
20 L
22 L
24 L
25 L
28 L
32 D
33 L
"""