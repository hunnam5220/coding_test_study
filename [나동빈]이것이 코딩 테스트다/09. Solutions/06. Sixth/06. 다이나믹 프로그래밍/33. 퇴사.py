from sys import stdin


def solution():
    n = int(stdin.readline())
    t, p = [], []

    mval = 0
    dp = [0] * (n + 1)
    for _ in range(n):
        a, b = map(int, stdin.readline().split())
        t.append(a)
        p.append(b)

    for i in range(n - 1, -1, -1):
        time = t[i] + i

        if time <= n:
            dp[i] = max(mval, dp[time] + p[i])
            mval = dp[i]
        else:
            dp[i] = mval

    return mval


print(solution())
