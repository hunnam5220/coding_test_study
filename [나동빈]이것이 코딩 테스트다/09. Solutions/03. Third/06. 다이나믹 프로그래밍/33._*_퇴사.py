from sys import stdin

t, p = [], []
n = int(stdin.readline())

dp = [0] * (n + 1)
max_val = 0

for i in range(n):
    a, b = map(int, stdin.readline().split())
    t.append(a)
    p.append(b)

for i in range(n - 1, -1, -1):
    time = i + t[i]
    if time <= n:
        dp[i] = max(dp[time] + p[i], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val)