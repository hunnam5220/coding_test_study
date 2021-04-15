from sys import stdin

n = int(stdin.readline().rstrip())
dp = [0] * (n + 1)
dp[0] = 1
idx2 = idx3 = idx5 = 0
n2, n3, n5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(n2, n3, n5)

    if dp[i] == n2:
        idx2 += 1
        n2 = dp[idx2] * 2

    if dp[i] == n3:
        idx3 += 1
        n3 = dp[idx3] * 3

    if dp[i] == n5:
        idx5 += 1
        n5 = dp[idx5] * 5

print(dp[n - 1])
