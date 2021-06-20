from sys import stdin


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n):
    parent = [0] * (n + 1)

    edges = []
    result = 0

    for i in range(1, n + 1):
        parent[i] = i

    x, y, z = [], [], []

    for i in range(1, n + 1):
        data = list(map(int, stdin.readline().split()))
        x.append((data[0], i))
        y.append((data[1], i))
        z.append((data[2], i))

    x.sort()
    y.sort()
    z.sort()

    for i in range(n - 1):
        # 비용, 간선 정보 1, 간선 정보 2
        edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
        edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
        edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

    edges.sort()

    for edge in edges:
        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return result


print(solution(int(stdin.readline())))

"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""
