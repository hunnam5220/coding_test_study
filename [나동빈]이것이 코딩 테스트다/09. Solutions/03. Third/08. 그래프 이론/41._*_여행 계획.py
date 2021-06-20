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
        parent[b] = b


def solution(n, m):
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i

    for i in range(n):
        data = list(map(int, stdin.readline().split()))
        for j in data:
            if j:
                union_parent(parent, i, j)

    plan = list(map(int, stdin.readline().split()))

    res = True
    for i in range(m - 1):
        if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
            res = False

    return "YES" if res else "NO"


N, M = map(int, stdin.readline().split())
print(solution(N, M))

"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

5 4
0 1 0 1 1
1 0 1 1 0 
0 1 0 0 0
1 1 0 0 0 
1 0 0 0 0
2 3 5 4

5 4
0 1 0 1 0
1 0 1 1 0 
0 1 0 0 0
1 1 0 0 0 
0 0 0 0 0
2 3 5 4
"""