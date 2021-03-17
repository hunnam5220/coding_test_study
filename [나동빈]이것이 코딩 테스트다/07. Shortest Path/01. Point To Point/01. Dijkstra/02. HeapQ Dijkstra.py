import heapq
from sys import stdin
INF = int(1e9)

n, m = map(int, stdin.readline().split())
start_node = int(stdin.readline().rstrip())
graph = [[] for _ in range(n)]
distance = [INF] * n

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a - 1].append([b - 1, c])
 

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


dijkstra(start_node)
for i in distance:
    if i == INF:
        print('INFINITY')
    else:
        print(i)