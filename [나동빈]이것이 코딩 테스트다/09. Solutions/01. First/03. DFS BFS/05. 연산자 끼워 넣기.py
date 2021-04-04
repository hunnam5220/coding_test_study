from sys import stdin
from itertools import product

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
a, b, c, d = map(int, stdin.readline().split())
cal = [list('+' * a), list('-' * b), list('*' * c), list('/' * d)]

# 모든 조합 구하기 구현

