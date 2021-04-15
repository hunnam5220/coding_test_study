from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
inf = int(1e9)
arr = [[inf] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    arr[a - 1][b - 1] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = 0

res = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][j] != inf or arr[j][i] != inf:
            cnt += 1

    if cnt == n:
        res += 1
print(res)

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""