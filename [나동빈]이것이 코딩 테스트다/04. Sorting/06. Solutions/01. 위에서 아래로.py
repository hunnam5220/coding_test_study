from sys import stdin

arr = []
for step in range(int(stdin.readline().rstrip())):
    arr.append(int(stdin.readline().rstrip()))

arr.sort(reverse=True)
print(' '.join(map(str, arr)))