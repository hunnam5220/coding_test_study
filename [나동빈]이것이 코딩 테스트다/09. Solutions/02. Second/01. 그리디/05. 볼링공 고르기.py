from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
result = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] != arr[j]:
            result += 1

print(result)
"""
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
"""