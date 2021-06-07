from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

distance = [-1 for _ in range(n + 1)]
distance[x] = 0
q = deque()
q.append(x)
visited = set()
visited.add(x)

while q:
    now = q.popleft()
    for next_ in graph[now]:
        if next_ not in visited:
            visited.add(next_)
            distance[next_] = distance[now] + 1
            q.append(next_)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
