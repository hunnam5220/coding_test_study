from sys import stdin
INF = int(1e9)

n, m = map(int, stdin.readline().split())
start_node = int(stdin.readline().rstrip())
graph = [[] for _ in range(n)]
visited = [False] * n
distance = [INF] * n

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a - 1].append((b - 1, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(n):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start_node):
    distance[start_node - 1] = 0
    visited[start_node - 1] = True
    for j in graph[start_node - 1]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start_node)

for step in distance:
    if step == INF:
        print('INFINITY')
    else:
        print(step)