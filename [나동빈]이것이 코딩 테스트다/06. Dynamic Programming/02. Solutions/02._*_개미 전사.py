from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))
d = [0] * 300001
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + arr[i])

print(max(d))