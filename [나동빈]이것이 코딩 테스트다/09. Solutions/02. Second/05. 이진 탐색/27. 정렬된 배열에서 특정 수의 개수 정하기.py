import bisect
from sys import stdin

n, x = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
k = bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)
if k == 0:
    print(-1)
else:
    print(k)

"""
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
"""