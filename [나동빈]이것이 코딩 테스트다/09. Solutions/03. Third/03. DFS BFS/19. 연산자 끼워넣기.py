from sys import stdin
from itertools import permutations

# 시간 줄이기 set

n = int(stdin.readline())
temp = ['+', '-', '*', '/']
num = list(map(int, stdin.readline().split()))
g = list(map(int, stdin.readline().split()))
gh = []

for i in range(4):
    for _ in range(g[i]):
        gh.append(temp[i])

p_gh = list(set(permutations(gh, n - 1)))

max_val = -1e9
min_val = 1e9

for step in p_gh:
    temp = num[0]
    for i in range(1, len(num)):
        x = step[i - 1]
        if x == '+':
            temp += num[i]

        elif x == '-':
            temp -= num[i]

        elif x == '*':
            temp *= num[i]

        elif x == '/':
            if temp < 0 or num[i] < 0:
                temp = abs(temp) // abs(num[i]) * -1
            else:
                temp //= num[i]

    max_val = max(temp, max_val)
    min_val = min(temp, min_val)

print(max_val)
print(min_val)
