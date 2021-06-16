from sys import stdin


def solution(s1, s2):
    n, m = len(s1), len(s2)

    ugly = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        ugly[i][0] = i

    for i in range(1, n + 1):
        ugly[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[j - 1] == s2[i - 1]:
                ugly[i][j] = ugly[i - 1][j - 1]

            else:
                ugly[i][j] = 1 + min(ugly[i - 1][j - 1], ugly[i - 1][j], ugly[i][j - 1])

    return ugly[m][n]


print(solution(stdin.readline().rstrip(), stdin.readline().rstrip()))