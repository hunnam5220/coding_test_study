from sys import stdin
from itertools import combinations
from collections import deque

n = int(stdin.readline().rstrip())
arr = list(stdin.readline().rstrip().split())
cal = []
d = {0: '+', 1: '-', 2: '*', 3: '/'}
result = []

for x, i in zip(list(map(int, stdin.readline().split())), range(4)):
    for _ in range(x):
        cal.append(d[i])

"""
arr 길이 - 1  >> cal 길이

arr 사이에 cal의 조합을 넣어서 계산하고

계산값이 있는 것들의 맥스 민 값을 출력

"""


print(max(result))
print(min(result))