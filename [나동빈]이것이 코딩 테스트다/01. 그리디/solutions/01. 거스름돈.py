from sys import stdin

n, m, k = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))
result = 0
cnt = 0
for x in range(m):
    if cnt < k:
        result += arr[-1]
        cnt +=1
    else:
        result += arr[-2]
        cnt = 0
print(result)