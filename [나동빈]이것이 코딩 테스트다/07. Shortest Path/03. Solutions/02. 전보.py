from sys import stdin
import heapq

INF = int(1e9)
n, m, c = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
distance = [INF] * n

for step in range(m):
    x, y, z = map(int, stdin.readline().split())
    graph[x - 1].append((y - 1, z))


def dijkstra(start_node):
    q = []

    heapq.heappush(q, (0, start_node - 1))

    distance[start_node - 1] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost

                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

result = 0
max_distance = 0
for step in distance:
    if step != INF:
        result += 1
        max_distance = max(max_distance, step)

print(result - 1, max_distance)