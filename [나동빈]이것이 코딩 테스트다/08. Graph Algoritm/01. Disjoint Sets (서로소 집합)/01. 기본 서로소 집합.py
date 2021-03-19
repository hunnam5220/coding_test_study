from sys import stdin


def find_parent(parent, x):
    if parent[x - 1] != x:
        return find_parent(parent, parent[x - 1])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b - 1] = a
    else:
        parent[a - 1] = b


v, e = map(int, stdin.readline().split())
parent = [0] * v

for i in range(v):
    parent[i] = i + 1


for i in range(e):
    a, b = map(int, stdin.readline().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합 : ', end=' ')
for i in range(v):
    print(find_parent(parent, i + 1), end=' ')

print()

print('부모 테이블 : ', end=' ')
for i in range(v):
    print(parent[i], end=' ')