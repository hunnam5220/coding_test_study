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


n, m = map(int, stdin.readline().split())
parent = [x for x in range(1, n + 1)]

for i in range(m):
    data = list(map(int, stdin.readline().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i, j)

plan = list(map(int, stdin.readline().split()))
result = True

for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

if result:
    print("YES")
else:
    print("NO")

"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""