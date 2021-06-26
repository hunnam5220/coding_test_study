from sys import stdin
from collections import deque


def solution():
    n = int(stdin.readline())
    data = list(map(int, stdin.readline().split()))
    indegree = [0] * (n + 1)

    arr = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(i + 1,  n):
            arr[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(stdin.readline())
    for _ in range(m):
        a, b = map(int, stdin.readline().split())

        if arr[a][b]:
            arr[a][b] = False
            arr[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            arr[a][b] = True
            arr[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    res = []
    cycle, certain = False, True

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            certain = False

        now = q.popleft()
        res.append(now)

        for j in range(1, n + 1):
            if arr[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")

    elif not certain:
        print("?")

    else:
        for i in res:
            print(i, end=' ')
        print()


for tc in range(int(stdin.readline())):
    solution()

"""
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
"""