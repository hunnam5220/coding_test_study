from sys import stdin


def solution(s1, s2):
    n, m = len(s1), len(s2)
    arr = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        arr[i][0] = i

    for i in range(1, n + 1):
        arr[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[j - 1] == s2[i - 1]:
                arr[i][j] = arr[i - 1][j - 1]

            else:
                arr[i][j] = 1 + min(arr[i - 1][j - 1], arr[i][j - 1], arr[i - 1][j])

    return arr[m][n]


print(solution("cat", "cut"))
print(solution("saturday", "sunday"))
print(solution("sunday", "saturday"))