from sys import stdin
from collections import deque


def solution(n):
    grade = list(map(int, stdin.readline().split()))

    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n):
            graph[grade[i]][grade[j]] = True
            indegree[grade[j]] += 1

    m = int(stdin.readline())

    for _ in range(m):
        a, b = map(int, stdin.readline().split())

        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1

        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()
    res = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            certain = False

        now = q.popleft()
        res.append(now)

        for j in range(1, n + 1):
            if graph[now][j]:
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
    solution(int(stdin.readline()))

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