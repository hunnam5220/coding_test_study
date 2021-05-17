from sys import stdin

a = list(stdin.readline().rstrip())
b = list(stdin.readline().rstrip())
len1 = len(a)
len2 = len(b)

dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    dp[i][0] = i

for j in range(1, len2 + 1):
    dp[0][j] = j

for x in range(1, len1 + 1):
    for y in range(1, len2 + 1):
        if a[x - 1] == b[y - 1]:
            dp[x][y] = dp[x - 1][y - 1]
        else:
            dp[x][y] = min(dp[x - 1][y - 1], dp[x - 1][y], dp[x][y - 1]) + 1

print(dp[len1][len2])

"""
sunday
saturday
>> 3
"""