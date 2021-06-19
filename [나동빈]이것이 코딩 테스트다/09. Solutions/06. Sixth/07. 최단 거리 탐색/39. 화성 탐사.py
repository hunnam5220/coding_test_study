from sys import stdin
import heapq


def solution():
    n = int(stdin.readline())
    inf = int(1e9)

    distance = [[inf] * n for _ in range(n)]
    arr = []
    for _ in range(n):
        arr.append(list(map(int, stdin.readline().split())))

    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

    x, y = 0, 0
    distance[x][y] = arr[x][y]
    q = []
    heapq.heappush(q, (arr[x][y], x, y))

    while q:
        dist, x, y = heapq.heappop(q)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            cost = dist + arr[nx][ny]
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    return distance[n - 1][n - 1]


for _ in range(int(stdin.readline())):
    print(solution())


















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