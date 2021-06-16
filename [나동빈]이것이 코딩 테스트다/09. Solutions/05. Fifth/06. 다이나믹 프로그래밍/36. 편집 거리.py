from sys import stdin


def solution(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for x in range(1, m + 1):
        dp[x][0] = x

    for x in range(1, n + 1):
        dp[0][x] = x

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    return dp[m][n]


print(solution("cat", "cut"))
print(solution("saturday", "sunday"))
print(solution("sunday", "saturday"))