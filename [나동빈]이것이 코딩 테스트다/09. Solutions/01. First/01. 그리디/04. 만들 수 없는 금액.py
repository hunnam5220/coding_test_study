from sys import stdin
from itertools import combinations as cmb

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
maximum = max(arr)
result = [x for x in range(1, maximum)]

for x in arr:
    if x in result:
        result.pop(result.index(x))

for x in range(1, n + 1):
    arr_cmb = list(cmb(arr, x))

    for y in arr_cmb:
        if sum(y) in result:
            result.pop(result.index(sum(y)))

print(min(result))

"""
5
3 2 1 1 9
"""