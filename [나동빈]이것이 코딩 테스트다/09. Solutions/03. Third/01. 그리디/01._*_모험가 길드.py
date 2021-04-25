from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
arr.sort()
group, cnt = 0, 0

for x in arr:
    group += 1
    if x == group:
        cnt += 1
        group = 0

print(cnt)
"""
5
2 3 1 2 2

10
1 1 2 2 3 3 4 4 5 5
"""