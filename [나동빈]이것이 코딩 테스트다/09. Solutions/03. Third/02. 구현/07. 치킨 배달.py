from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())

city = [[0] * n for _ in range(n)]
house = []
chick = []

for x in range(n):
    temp = list(map(int, stdin.readline().split()))
    for y in range(len(temp)):
        if temp[y] == 1:
            house.append([x, y])
        elif temp[y] == 2:
            chick.append([x, y])

chickens = list(combinations(chick, m))

result =[int(1e9)]


def check_distance(cc):
    distance = 0
    for h in house:
        tmp = int(1e9)
        x1, y1 = h
        for c in cc:
            x2, y2 = c
            tmp = min(tmp, abs(x1 - x2) + abs(y1 - y2))

        distance += tmp
    result[0] = min(result[0], distance)


for cc in chickens:
    check_distance(cc)

print(result[0])