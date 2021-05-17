from sys import stdin
from bisect import bisect_left, bisect_right


n, x = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().split()))


def get_count_number(arr, a, b):
    result = bisect_right(arr, b) - bisect_left(arr, a)
    return result if result > 0 else -1


print(get_count_number(arr, x, x))


"""
7 2
1 1 2 2 2 2 4

7 4
1 1 2 2 2 2 3
"""