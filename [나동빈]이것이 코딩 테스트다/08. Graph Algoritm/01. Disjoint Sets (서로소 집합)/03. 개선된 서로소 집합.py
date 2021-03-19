from sys import stdin


def find_parent(parent, x):
    """ 부모 노드 찾기 - 경로 압축 """

    """ 부모 노드 리스트와 x가 같지 않으면"""
    if parent[x - 1] != x:
        """ 부모 노드 리스트를 직접 바꿔버림 """
        parent[x - 1] = find_parent(parent, parent[x - 1])
    return parent[x - 1]


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