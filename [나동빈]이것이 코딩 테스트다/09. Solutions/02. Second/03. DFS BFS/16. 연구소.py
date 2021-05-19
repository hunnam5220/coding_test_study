from sys import stdin

n, m = map(int, stdin.readline().split())

board = []

for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0 , -1]

cnt = 0
result = 0


def dfs(count):
    global result
    if count == 3:
        temp = [item[:] for item in board]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    insfection(temp, i, j)

        result = max(result, get_score(temp))
        return

    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                board[x][y] += 1
                count += 1
                dfs(count)
                count -= 1
                board[x][y] -= 1


def get_score(temp):
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1

    return score


def insfection(temp, x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                insfection(temp, nx, ny)


dfs(0)
print(result)