from sys import stdin

n = int(stdin.readline())
t, p = [], []
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    t.append(a)
    p.append(b)


val = 0
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    time = t[i] + i

    if time <= n:
        dp[i] = max(val, dp[time] + p[i])
        val = dp[i]
    else:
        dp[i] = val

print(val)