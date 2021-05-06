from sys import stdin
from itertools import combinations
from itertools import permutations

n, m = map(int, stdin.readline().split())
chicken_xy = []
house_xy = []

for x in range(n):
    data = list(map(int, stdin.readline().split()))
    for y in range(len(data)):
        if data[y] == 1:
            house_xy.append([x, y])

        elif data[y] == 2:
            chicken_xy.append([x, y])

result = 1e9

for chicken in list(combinations(chicken_xy, m)):
    tmp_ans = 0
    for house in house_xy:
        x1, y1 = house
        temp_val = 1e9
        for cc in chicken:
            x2, y2 = cc
            temp_val = min(temp_val, abs(x1 - x2) + abs(y1 - y2))

        tmp_ans += temp_val

    result = min(tmp_ans, result)

print(result)
