from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

visited = [x]
q = deque()
q.append(x)

distance = [-1] * (n + 1)
distance[x] = 0

while q:
    now = q.popleft()

    if distance[now] + 1 > k:
        break

    for next_node in graph[now]:
        if next_node not in visited and distance[next_node] == -1:
            visited.append(next_node)
            distance[next_node] = distance[now] + 1
            q.append(next_node)


check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)