from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
arr.sort()
t = 1

for x in arr:
    if t < x:
        break
    t += x

print(t)