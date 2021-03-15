from sys import stdin

INF = int(1e9)

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

graph = [[INF] * n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a - 1][b - 1] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(n):
    for b in range(n):
        if graph[a][b] == INF:
            print("I", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()