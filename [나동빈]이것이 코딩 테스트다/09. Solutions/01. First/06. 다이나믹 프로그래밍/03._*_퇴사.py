from sys import stdin

n = int(stdin.readline().rstrip())
t, p = [], []
max_val = 0
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    t.append(x)
    p.append(y)

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    time = t[i] + i

    if time <= n:
        dp[i] = max(max_val, dp[time] + p[i])
        max_val = dp[i]

    else:
        dp[i] = max_val

print(max_val)

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
"""