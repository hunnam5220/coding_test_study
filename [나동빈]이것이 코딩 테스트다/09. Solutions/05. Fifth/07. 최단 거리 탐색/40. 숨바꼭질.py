from sys import stdin
from collections import deque


def solution(n, m):
    inf = int(1e9)
    arr = [[] for _ in range(n + 1)]
    distance = [inf] * (n + 1)

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        arr[a].append((b, 1))
        arr[b].append((a, 1))

    start = 1
    distance[start] = 0
    q = deque()
    q.append((start, 0))

    while q:
        now, d = q.popleft()

        for i in arr[now]:
            if i[1] < d or distance[i[0]] != inf:
                continue

            cost = i[1] + d
            distance[i[0]] = cost
            q.append((i[0], cost))

    dist = max(distance[1:])
    node = distance.index(dist)
    res = []

    for i in range(1, n + 1):
        if distance[i] == dist:
            res.append(i)

    return node, dist, len(res)


N, M = map(int, stdin.readline().split())
n, d, l = solution(N, M)
print(n, d, l)
"""
Î
"""