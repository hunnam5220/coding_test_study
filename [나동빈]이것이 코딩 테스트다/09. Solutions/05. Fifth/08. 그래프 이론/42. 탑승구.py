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


def solution(g, p):
    parent = [0] * (g + 1)
    
    return


G, P = map(int, stdin.readline().split())
print(solution(G, P))

"""
4
3
4
1
1
"""