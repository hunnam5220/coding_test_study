from sys import stdin


def find_parent(parent, x):
    """ 부모를 찾는 함수 """

    """ 만약 리스트의 x 번째 요소가 x와 같지 않다면 재귀적으로 호출"""
    if parent[x - 1] != x:
        return find_parent(parent, parent[x - 1])
    return x


def union_parent(parent, a, b):
    """ 두 원소가 속한 집합을 합치는 함수 """

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    """ 더 작은 번호의 노드가 부모 노드가 된다. """
    if a < b:
        parent[b - 1] = a
    else:
        parent[a - 1] = b


""" 노드 개수와 간선 수를 입력 받음 """
v, e = map(int, stdin.readline().split())
""" 부모 노드 데이터를 담을 리스트 생성 """
parent = [0] * v

""" 각 노드의 부모 노드 번호를 자신의 번호로 초기화 """
for i in range(v):
    parent[i] = i + 1

""" 두 수를 입력 받아 union 함수에 넣음 """
for i in range(e):
    a, b = map(int, stdin.readline().split())
    union_parent(parent, a, b)

""" 출력 """
print('각 원소가 속한 집합 : ', end=' ')
for i in range(v):
    print(find_parent(parent, i + 1), end=' ')

print()

print('부모 테이블 : ', end=' ')
for i in range(v):
    print(parent[i], end=' ')
