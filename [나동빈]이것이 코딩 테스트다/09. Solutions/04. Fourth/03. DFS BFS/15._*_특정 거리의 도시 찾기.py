from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

dis = [-1] * (n + 1)
dis[x] = 0


def bfs(x):

    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dis[i] == -1:
                q.append(i)
                dis[i] = dis[now] + 1


bfs(x)
c = False
for i in range(1, n + 1):
    if dis[i] == k:
        print(i)
        c = True

if not c:
    print(-1)