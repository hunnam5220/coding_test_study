from sys import stdin


def solution(n, arr):
    dp = [0] * (n + 1)
    val = 0

    for i in range(n - 1, -1, -1):
        t = arr[i][0] + i

        if t <= n:
            dp[i] = max(dp[t] + arr[i][1], val)
            val = dp[i]
        else:
            dp[i] = val

    return val


num = int(stdin.readline())

print(solution(num, [list(map(int, stdin.readline().split())) for _ in range(num)]))