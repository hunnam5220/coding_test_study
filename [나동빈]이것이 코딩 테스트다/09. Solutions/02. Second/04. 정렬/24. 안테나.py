from sys import stdin

n = int(stdin.readline())
house = list(map(int, stdin.readline().split()))
house.sort()

distance = [1e9 for _ in range(n)]

if n % 2 == 0:
    idx = n // 2 - 1
else:
    idx = n // 2

print(house[idx])