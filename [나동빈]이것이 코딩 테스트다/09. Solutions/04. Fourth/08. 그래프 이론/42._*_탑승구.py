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
    for i in range(1, g + 1):
        parent[i] = i

    res = 0

    for _ in range(p):
        # 현재 비행기의 탑승구의 루트 확인
        data = find_parent(parent, int(stdin.readline()))

        # 현재 루트가 0이라면, 종료
        if data == 0:
            break

        # 그렇지 않다면 바로 왼쪽의 집합과 합치기
        union_parent(parent, data, data - 1)
        res += 1

    return res


print(solution(int(stdin.readline()), int(stdin.readline())))

"""
4
3
4
1
1
"""