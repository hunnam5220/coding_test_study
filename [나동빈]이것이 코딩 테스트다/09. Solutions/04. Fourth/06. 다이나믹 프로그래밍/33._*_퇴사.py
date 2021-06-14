from sys import stdin

n = int(stdin.readline())
t, p = [], []

for i in range(n):
    a, b = map(int, stdin.readline().split())
    t.append(a)
    p.append(b)

max_val = 0

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    time = i + t[i]
    if time <= n:
        dp[i] = max(dp[time] + p[i], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val)