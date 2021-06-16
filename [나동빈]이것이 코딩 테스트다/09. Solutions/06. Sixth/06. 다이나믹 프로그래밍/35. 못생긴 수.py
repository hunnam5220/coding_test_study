from sys import stdin


def solution(n):
    i2, i3, i5 = 0, 0, 0
    n2, n3, n5 = 2, 3, 5

    dp = [1]

    for i in range(n):
        k = min(n2, n3, n5)
        dp.append(k)

        if k == n2:
            i2 += 1
            n2 = dp[i2] * 2

        if k == n3:
            i3 += 1
            n3 = dp[i3] * 3

        if k == n5:
            i5 += 1
            n5 = dp[i5] * 5

    return dp[n - 1]


print(solution(int(stdin.readline())))
