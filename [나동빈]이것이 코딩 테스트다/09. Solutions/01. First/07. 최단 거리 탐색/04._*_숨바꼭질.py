from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())
inf = int(1e9)
distance = [inf] * n
arr = [[] * n for _ in range(n)]
start = 1

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    arr[a - 1].append((b, 1))
    arr[b - 1].append((a, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start - 1] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now - 1] < dist:
            continue

        for i in arr[now - 1]:
            cost = dist + i[1]

            if cost < distance[i[0] - 1]:
                distance[i[0] - 1] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)


max_node = 0
max_distance = 0
result = []

for i in range(n):
    if max_distance < distance[i]:
        max_node = i + 1
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))
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
