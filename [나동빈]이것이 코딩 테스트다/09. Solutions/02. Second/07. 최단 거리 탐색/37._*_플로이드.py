from sys import stdin


n, m = int(stdin.readline()), int(stdin.readline())
inf = 1e9
graph = [[inf] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())

    # 가장 짧은 노선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == inf:
            print(0, end=' ')

        else:
            print(graph[a][b], end=' ')
    print()