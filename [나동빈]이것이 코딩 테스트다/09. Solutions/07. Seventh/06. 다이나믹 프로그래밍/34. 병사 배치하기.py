from sys import stdin


def solution(n, arr):
    arr.reverse()

    dp = [1] * (n + 1)

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return n - max(dp)


print(solution(int(stdin.readline()), list(map(int, stdin.readline().split()))))