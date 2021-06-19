from sys import stdin
from collections import deque


def solution():
    n, m = map(int, stdin.readline().split())

    arr = [[] for _ in range(n + 1)]
    start = 1
    inf = int(1e9)

    distance = [inf] * (n + 1)

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        arr[a].append((b, 1))
        arr[b].append((a, 1))

    q = deque()
    q.append((start, 0))
    distance[start] = 0

    while q:
        now, dist = q.popleft()

        for i in arr[now]:
            if dist > i[1] or distance[i[0]] != inf:
                continue

            cost = dist + i[1]
            distance[i[0]] = cost
            q.append((i[0], cost))

    dist = max(distance[1:])
    node = distance.index(dist)
    res = []

    for i in range(1, n + 1):
        if dist == distance[i]:
            res.append(i)

    return node, dist, len(res)


n, d, l = solution()
print(n, d, l)

"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""