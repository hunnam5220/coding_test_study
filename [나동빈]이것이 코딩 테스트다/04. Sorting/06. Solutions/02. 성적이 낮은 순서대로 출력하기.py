from sys import stdin

arr = []
for step in range(int(stdin.readline().rstrip())):
    x, y = stdin.readline().rstrip().split()
    arr.append([x, int(y)])


def setting(data):
    return data[1]


arr.sort(key=setting)
for step in arr:
    print(step[0], end=' ')
