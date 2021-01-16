from sys import stdin

x, y = map(int, stdin.readline().split())
arr = []

for step in range(x):
    arr.append(list(map(int, stdin.readline().split())))

print(min(arr[x-1]))