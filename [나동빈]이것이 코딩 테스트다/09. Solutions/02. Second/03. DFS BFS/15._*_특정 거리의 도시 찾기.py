from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0


def bfs(x):
    q = deque([x])

    while q:
        now = q.popleft()

        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                q.append(next_node)

    check = False
    for i in range(n):
        if distance[i] == k:
            print(i)
            check = True

    if not check:
        print(-1)


bfs(x)