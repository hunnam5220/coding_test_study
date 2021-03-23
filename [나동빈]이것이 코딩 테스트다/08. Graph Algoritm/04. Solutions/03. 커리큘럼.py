from sys import stdin
from collections import deque
from copy import deepcopy

n = int(stdin.readline().rstrip())
graph = [[] for x in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, stdin.readline().split()))
    time[i] = data[0]

    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i - 1] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


topology_sort()

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""