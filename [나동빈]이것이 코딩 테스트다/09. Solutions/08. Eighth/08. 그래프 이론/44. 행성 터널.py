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
    for i in range(1, n + 1):
        parent[i] = i

    x, y, z, edges = [], [], [], []

    for i in range(1, n + 1):
        a, b, c = map(int, stdin.readline().split())
        x.append((a, i))
        y.append((b, i))
        z.append((c, i))

    x.sort()
    y.sort()
    z.sort()

    for i in range(n - 1):
        edges.append((x[i + 1][0] - x[i][0], x[i + 1][1], x[i][1]))
        edges.append((y[i + 1][0] - y[i][0], y[i + 1][1], y[i][1]))
        edges.append((z[i + 1][0] - z[i][0], z[i + 1][1], z[i][1]))

    edges.sort()
    res = 0

    for edge in edges:
        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            res += cost

    return res


print(solution(int(stdin.readline())))

"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""