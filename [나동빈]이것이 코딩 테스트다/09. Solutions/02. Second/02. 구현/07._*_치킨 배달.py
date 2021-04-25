from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
house = []
chiken = []
city = []

for _ in range(n):
    city.append(list(map(int, stdin.readline().split())))

for x in range(n):
    for y in range(n):
        if city[x][y] == 1:
            house.append([x, y])
        if city[x][y] == 2:
            chiken.append([x, y])

comb_s = list(combinations(chiken, m))


def get_distance(comb):
    result = 0

    for hx, hy in house:
        tmp = 1e9
        for cx, cy in comb:
            tmp = min(abs(hx - cx) + abs(hy - cy), tmp)
        result += tmp

    return result


ans = 1e9
for comb in comb_s:
    ans = min(ans, get_distance(comb))

print(ans)
