from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
cnt = 0
for x in range(n):
    for y in range(x + 1, n):
        if arr[x] != arr[y]:
            cnt += 1

print(cnt)

"""
# 8
5 3
1 3 2 3 2

# 25
8 5
1 5 4 3 2 4 5 2
"""