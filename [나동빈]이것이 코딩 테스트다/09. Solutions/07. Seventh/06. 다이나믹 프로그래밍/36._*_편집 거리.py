from sys import stdin


def solution(s1, s2):
    n, m = len(s1), len(s2)

    s = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        s[i][0] = i

    for i in range(1, n + 1):
        s[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[j - 1] == s2[i - 1]:
                s[i][j] = s[i - 1][j - 1]

            else:
                s[i][j] = 1 + min(s[i - 1][j - 1], s[i][j - 1], s[i - 1][j])

    return s[m][n]


print(solution(stdin.readline().rstrip(), stdin.readline().rstrip()))