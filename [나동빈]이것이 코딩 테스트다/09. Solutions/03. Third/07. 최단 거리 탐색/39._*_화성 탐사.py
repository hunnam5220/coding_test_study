from sys import stdin
import heapq

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def solution(tc):
    for _ in range(tc):
        n = int(stdin.readline())
        graph = []
        x, y = 0, 0
        q = []
        inf = int(1e9)

        for _ in range(n):
            graph.append(list(map(int, stdin.readline().split())))

        distance = [[inf] * n for _ in range(n)]

        heapq.heappush(q, (graph[0][0], x, y))

        while q:
            dist, x, y = heapq.heappop(q)

            if dist > distance[x][y]:
                continue

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    cost = graph[nx][ny] + dist
                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost
                        heapq.heappush(q, (cost, nx, ny))

                else:
                    continue

        print(distance[n - 1][n - 1])


solution(int(stdin.readline()))


"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""