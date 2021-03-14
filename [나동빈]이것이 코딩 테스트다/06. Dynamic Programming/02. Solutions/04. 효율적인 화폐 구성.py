from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [int(stdin.readline().rstrip()) for x in range(n)]
d = [10001] * (m + 1)
d[0] = 10001

for x in arr:
    for y in range(1, m + 1):
        if m % x == 0 and d[y] > m // x:
            d[y] = m // x

if d[m] == 10001:
    print(-1)
else:
    print(d[m])