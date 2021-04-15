from sys import stdin

arr = [1, 2, 3, 5]
dp = []
for x in arr:
    for y in arr:
        if x * y not in dp:
            dp.append(x * y)

n = int(stdin.readline().rstrip())
start = 1
end = 4

for step in range(n // 4):
    for i in dp[start:end]:
        for j in range(len(arr)):
            if (i * arr[j]) not in dp:
                dp.append(i * arr[j])
                end += 1
                start += 1

    dp.sort()

print(dp[n - 1])
