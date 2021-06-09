from sys import stdin
from bisect import bisect_left, bisect_right

n, x = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
print(abs(bisect_left(arr, x) - bisect_right(arr, x)))
