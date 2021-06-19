from collections import deque
from sys import stdin


def solution(n, m):
    inf = int(1e9)
    arr = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        arr[a].append((b, 1))
        arr[b].append((a, 1))

    distance = [inf] * (n + 1)
    q = deque()
    start = 1
    distance[start] = 0

    q.append((start, 0))

    while q:
        now, d = q.popleft()

        for i in arr[now]:
            cost = d + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.append((i[0], cost))

    dist = max(distance[1:])
    node = distance.index(dist)
    res = [x for x in distance if x == dist]

    return node, dist, len(res)


N, M = map(int, stdin.readline().split())
n, d, l = solution(N, M)
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
