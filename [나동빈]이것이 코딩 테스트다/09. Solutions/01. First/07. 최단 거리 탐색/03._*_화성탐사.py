from sys import stdin
import heapq

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
inf = int(1e9)
for _ in range(int(stdin.readline().rstrip())):
    n = int(stdin.readline().rstrip())
    arr = []
    for __ in range(n):
        arr.append(list(map(int, stdin.readline().rstrip().split())))

    distance = [[inf] * n for _ in range(n)]

    x, y = 0, 0
    q = [(arr[x][y], x, y)]
    distance[x][y] = arr[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + arr[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n - 1][n - 1])

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