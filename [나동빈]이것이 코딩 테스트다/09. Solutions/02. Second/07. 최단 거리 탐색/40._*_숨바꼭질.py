from sys import stdin
import heapq


def solution(nm):
    n, m = nm
    inf = int(1e9)
    graph = [[] for _ in range(n + 1)]
    distance = [inf] * (n + 1)
    start = 1

    for i in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    dijkstra(start, distance, graph)

    max_node = 0
    max_distance = 0
    result = []

    for i in range(1, n + 1):
        if max_distance < distance[i]:
            max_node = i
            max_distance = distance[i]
            result = [max_node]

        elif max_distance == distance[i]:
            result.append(i)

    return max_node, max_distance, len(result)


def dijkstra(start, distance, graph):
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


node, dis, l = solution(list(map(int, stdin.readline().split())))
print(node, dis, l)

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