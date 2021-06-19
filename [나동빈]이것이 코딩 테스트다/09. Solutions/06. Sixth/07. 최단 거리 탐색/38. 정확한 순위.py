from sys import stdin


def solution(n, m):
    inf = int(1e9)
    arr = [[inf] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                arr[i][j] = 0

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        arr[a][b] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    res = 0

    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if arr[i][j] != inf or arr[j][i] != inf:
                cnt += 1

        if cnt == n:
            res += 1

    return res


N, M = map(int, stdin.readline().split())
print(solution(N, M))


"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""