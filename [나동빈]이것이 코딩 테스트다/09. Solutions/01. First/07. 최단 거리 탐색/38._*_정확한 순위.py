from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
inf = int(1e3)
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


# 학생 한명씩 도달 할 수 있는지 체크
for x in range(n):
    cnt = 0
    for y in range(n):
        # 1이 4? 혹은 4가 1? 양방향으로 체크함
        if arr[x][y] != inf or arr[y][x] != inf:
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