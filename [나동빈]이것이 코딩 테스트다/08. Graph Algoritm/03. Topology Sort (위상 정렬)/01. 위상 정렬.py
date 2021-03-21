from collections import deque
from sys import stdin

v, e = map(int, stdin.readline().split())
indegree = [0] * v
graph = [[] for _ in range(v)]

for _ in range(e):
    a, b = map(int, stdin.readline().split())
    graph[a - 1].append(b)
    indegree[b - 1] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(v):
        if indegree[i] == 0:
            q.append(i)

            