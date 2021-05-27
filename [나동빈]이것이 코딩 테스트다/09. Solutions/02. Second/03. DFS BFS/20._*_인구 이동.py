from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())

board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0


def process(x, y, index):
    # 시작 국가 넣기
    united = [(x, y)]

    q = deque()
    q.append((x, y))

    # 연합 번호 1
    union[x][y] = 1
    summary = board[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # l보다 크거나 같고 r보다 작거나 같으면 수행
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    q.append((x, y))
                    union[nx][ny] = index
                    summary += board[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united:
        board[i][j] = summary // count

    return count


total_count = 0

while 1:
    # 연합 표시용으로 반든 리스트
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            # 연합 표시 안되어 있는 곳이면 ㄱㄱ
            if union[i][j] == -1:
                # 연합 표시 하러 ㄱㄱ
                process(i, j, index)
                index += 1

    if index == n * n:
        break
    total_count += 1

print(total_count)
