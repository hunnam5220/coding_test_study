from sys import stdin


def find_parent(parent, x):
    if parent[x - 1] != x:
        parent[x - 1] = find_parent(parent, parent[x - 1])
    return parent[x - 1]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[a - 1] = b
    else:
        parent[b - 1] = a


v, e = map(int, stdin.readline().split())
parent = [0] * v

for i in range(v):
    parent[i] = i + 1

cycle = False

for i in range(e):
    a, b = map(int, stdin.readline().split())

    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")

else:
    print("사이클 미발생")