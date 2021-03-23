from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
arr.sort(reverse=True)
cnt = 0

while arr:
    m = max(arr)
    tmp = []
    for _ in range(m):
        tmp.append(arr.pop(arr.index(max(arr))))

    if len(tmp) >= m:
        cnt += 1

print(cnt)
"""
5
2 3 1 2 2
"""