from sys import stdin

n = int(stdin.readline())
t, p = [], []

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    t.append(a)
    p.append(b)

mval = 0
dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    time = i + t[i]

    if time <= n:
        dp[i] = max(dp[time] + p[i], mval)
        mval = dp[i]

    else:
        dp[i] = mval

print(mval)
