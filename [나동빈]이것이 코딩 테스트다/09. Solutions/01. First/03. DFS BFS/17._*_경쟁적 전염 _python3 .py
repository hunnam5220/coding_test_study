# BFS로 풀어보기
from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
graph = []
# 데이터 리스트 생성
data = []

for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))
    # 바이러스 존재하면 시간 정보, 바이러스 좌표 삽입
    for q in range(n):
        if graph[i][q] != 0:
            data.append([graph[i][q], 0, i, q])

data.sort()
q = deque(data)

ts, tx, ty = map(int, stdin.readline().split())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

while q:
    v, s, x, y = q.popleft()
    if s == ts:
        break

    for step in range(4):
        nx = x + dx[step]
        ny = y + dy[step]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                q.append([v, s + 1, nx, ny])

print(graph[tx - 1][ty - 1])
