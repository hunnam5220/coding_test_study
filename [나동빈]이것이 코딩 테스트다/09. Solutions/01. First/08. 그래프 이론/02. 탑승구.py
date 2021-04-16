from sys import stdin


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(stdin.readline().rstrip())
p = int(stdin.readline().rstrip())
parent = [0] * (g + 1)

for i in range(1, g+1):
    parent[i] = i

result = 0
for _ in range(p):
    k = find_parent(parent, int(stdin.readline().rstrip()))
    if k == 0:
        break

    union_parent(parent, k, k-1)
    result += 1

print(result)

"""
4
3
4
1
1


4
6
2
2
3
3
4
4
"""