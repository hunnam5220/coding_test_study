from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().rstrip().split())
houses, bbqs = [], []

for x in range(n):
    data = list(map(int, stdin.readline().split()))
    for y in range(len(data)):
        if data[y] == 1:
            houses.append([x + 1, y + 1])
        elif data[y] == 2:
            bbqs.append([x + 1, y + 1])

comb_bbq = list(combinations(bbqs, m))

result = 1e9

for bbqs in comb_bbq:
    tmp1 = 0
    for house in houses:
        tmp2 = 1e9
        for bbq in bbqs:
            tmp2 = min(tmp2, abs(house[0]-bbq[0]) + abs(house[1]-bbq[1]))

        tmp1 += tmp2

    result = min(tmp1, result)

print(result)