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


def solution(n, m):
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    edges = []

    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        edges.append((c, a, b))

    edges.sort()
    total = 0
    k = 0

    for edge in edges:
        cost, a, b = edge
        total += cost

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            k += cost

    return total - k


N, M = map(int, stdin.readline().split())
print(solution(N, M))

"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""