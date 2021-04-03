# BFS로 풀어보기

from sys import stdin

n, k = map(int, stdin.readline().split())
graph = []
# 데이터 리스트 생성


for step in range(n):
    pp = list(map(int, stdin.readline().split()))
    # 바이러스 존재하면 바이러스 좌표, 시간 정보 삽입

tmp = [item[:] for item in graph]

s, x, y = map(int, stdin.readline().split())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def infection(number, nx, ny):
    for i in range(4):
        kx, ky = nx + dx[i], ny + dy[i]

        if (n > kx > -1 and n > ky > -1) and tmp[kx][ky] == 0:
            tmp[kx][ky] = number
            zero[0] -= 1


for step in range(s):
    for number in range(1, k + 1):
        for nx in range(n):
            for ny in range(n):
                if graph[nx][ny] == number:
                    infection(number, nx, ny)

        if zero[0] == 0:
            break
    graph = [item[:] for item in tmp]

print(tmp[x - 1][y - 1])
