from sys import stdin

arr = []

for _ in range(int(stdin.readline())):
    data = list(stdin.readline().split())
    data[1:] = map(int, data[1:])
    arr.append(data)

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])