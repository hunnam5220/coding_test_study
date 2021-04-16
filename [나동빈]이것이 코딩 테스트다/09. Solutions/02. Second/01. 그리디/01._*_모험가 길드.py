from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
arr.sort()
cnt, result = 0, 0

for i in arr:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)