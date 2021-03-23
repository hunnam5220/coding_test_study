from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
cnt = 0

chk_list = list(combinations(arr, 2))
for chk in chk_list:
    if chk[0] != chk[1]:
        cnt += 1

print(cnt)


"""
5 3
1 3 2 3 2
"""

"""
8 5
1 5 4 3 2 4 5 2
"""