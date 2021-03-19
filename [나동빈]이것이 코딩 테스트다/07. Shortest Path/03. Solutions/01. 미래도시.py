from sys import stdin

INF = int(1e9)
n, m = map(int, stdin.readline().split())
graph = [[INF] * n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if x == y:
            graph[x][y] = 0

for step in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

x, k = map(int, stdin.readline().split())

for x in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][x] + graph[x][b])

distance = graph[0][k - 1] + graph[k - 1][x - 1]
if distance >= INF:
    print(-1)
else:
    print(distance)
