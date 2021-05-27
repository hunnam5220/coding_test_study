from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = [0]


def get_score(temp):
    score = 0
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 0:
                score += 1
    return score


def insfection(x, y, temp):
    q = deque()
    q.append((x, y))

    while q:
        ix, iy = q.popleft()
        for i in range(4):
            nx = dx[i] + ix
            ny = dy[i] + iy

            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))


def solution(cnt):
    if cnt == 3:
        temp = [item[:] for item in board]
        for x in range(n):
            for y in range(m):
                if board[x][y] == 2:
                    insfection(x, y, temp)

        score_val = get_score(temp)
        result[0] = max(result[0], score_val)

    else:
        for x in range(n):
            for y in range(m):
                if board[x][y] == 0:
                    board[x][y] = 1
                    cnt += 1
                    solution(cnt)
                    board[x][y] = 0
                    cnt -= 1


solution(0)
print(result[0])