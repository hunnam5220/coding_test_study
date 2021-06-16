from sys import stdin


def solution():
    n = int(stdin.readline())
    arr = []

    for i in range(n):
        arr.append(list(map(int, stdin.readline().split())))

    dp = [0] * (n + 1)
    val = 0

    for i in range(n - 1, -1, -1):
        time = arr[i][0] + i
            dp[i] = max(arr[i][1] + dp[time], val)
            val = dp[i]
        else:
            dp[i] = val
    return val


print(solution())
