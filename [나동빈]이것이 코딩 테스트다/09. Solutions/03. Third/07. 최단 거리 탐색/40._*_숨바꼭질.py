from sys import stdin
import heapq


def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def solution():
    n, m = map(int, stdin.readline().split())

    graph = [[] for _ in range(n + 1)]
    start = 1
    inf = int(1e9)

    distance = [inf] * (n + 1)

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    dijkstra(start, graph, distance)

    max_node, max_dist, res = 0, 0, []

    for i in range(1, n + 1):
        if max_dist < distance[i]:
            max_dist = distance[i]
            max_node = i
            res = [i]

        elif max_dist == distance[i]:
            res.append(i)

    return max_node, max_dist, len(res)


node, dist, l = solution()
print(node, dist, l)

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