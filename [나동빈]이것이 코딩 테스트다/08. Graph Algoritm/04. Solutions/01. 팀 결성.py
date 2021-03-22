from sys import stdin


def find_parent(parent, x):
    if parent[x - 1] != x:
        parent[x - 1] = find_parent(parent, parent[x - 1])
    return parent[x - 1]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b - 1] = a
    else:
        parent[a - 1] = b


e, v = map(int, stdin.readline().split())
parent = [_ for _ in range(1, e + 1)]
graph = [[] for _ in range(e)]

for x in range(v):
    oper, a, b = map(int, stdin.readline().split())

    if oper:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')

    else:
        union_parent(parent, a, b)

"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""