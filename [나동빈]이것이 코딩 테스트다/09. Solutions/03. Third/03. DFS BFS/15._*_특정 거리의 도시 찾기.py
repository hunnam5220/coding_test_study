from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for step in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

visited = []
result = []
distance = [-1] * (n + 1)
distance[x] = 0

q = deque()
q.append(x)


while q:
    now = q.popleft()

    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)


check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
