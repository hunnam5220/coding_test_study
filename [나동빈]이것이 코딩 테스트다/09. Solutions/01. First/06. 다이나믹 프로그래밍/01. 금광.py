from sys import stdin
from collections import deque

test_case = int(stdin.readline().rstrip())
dx = [-1, 0, 1]
dy = [1, 1, 1]


def get_road(pos):
    next_value = -int(1e9)
    x, y = pos
    next_roads = '0'
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] > next_value:
                next_value = arr[nx][ny]
                next_roads = (nx, ny, next_value)
    return next_roads if len(next_roads) != 1 else False


for z in range(test_case):
    n, m = map(int, stdin.readline().split())
    input_arr = list(map(int, stdin.readline().split()))
    arr = [input_arr[k * m:(k + 1) * m] for k in range(n)]
    result = [0]
    visited = []

    for step in range(n):
        i, j = step, 0
        visited = []
        q = deque([(i, j, arr[i][j])])
        score = 0
        while q:
            tmp = q.popleft()
            pos = tmp[0:2]
            score += tmp[-1]
            visited.append(pos)
            next_roads = get_road(pos)
            if next_roads:
                if next_roads[0:2] not in visited:
                    q.append(next_roads)

            if pos[1] == m - 1:
                if result[0] < score:
                    result[0] = score
                break
    print(result[0])
"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""