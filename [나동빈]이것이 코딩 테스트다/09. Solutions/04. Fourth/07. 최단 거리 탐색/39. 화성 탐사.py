from sys import stdin
import heapq


def solution(tc):
    for _ in range(tc):
        n = int(stdin.readline())
        board = []
        for __ in range(n):
            board.append(list(map(int, stdin.readline().split())))

        inf = int(1e9)
        arr = [[inf] * n for ___ in range(n)]
        q = []
        x, y = 0, 0
        arr[x][y] = board[x][y]

        heapq.heappush(q, (board[x][y], x, y))

        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

        while q:
            c, x, y = heapq.heappop(q)
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if nx < 0 or nx >= n or ny >= n or ny < 0:
                    continue

                cost = c + board[nx][ny]

                if cost < arr[nx][ny]:
                    arr[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

        print(arr[n - 1][n - 1])


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