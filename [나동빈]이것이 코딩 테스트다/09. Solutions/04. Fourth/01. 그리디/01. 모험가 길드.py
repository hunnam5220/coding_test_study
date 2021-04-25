from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
arr.sort()
cnt = 0
result = 0

for x in arr:
    cnt += 1
    if cnt == x:
        result += 1
        cnt = 0

print(result)

"""
5
2 3 1 2 2

5
4 1 2 3 1

5
4 1 2 2 1
"""