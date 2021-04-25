from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
arr.sort()

target = 1

for x in arr:
    if target < x:
        break
    else:
        target += x

print(target)


"""
5
3 2 1 1 9


10
8 3 6 7 7 9 3 1 1 2
"""