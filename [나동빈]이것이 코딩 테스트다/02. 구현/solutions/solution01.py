from sys import stdin

n = int(stdin.readline().rstrip())
xy = [1, 1]

arr = list(stdin.readline().split())

for x in arr:
    if x == 'U':
        if xy[0] == 1:
            pass
        else:
            xy[0] -= 1

    elif x == 'L':
        if xy[1] == 1:
            pass
        else:
            xy[1] -= 1

    elif x == 'R':
        if xy[1] > 5:
            pass
        else:
            xy[1] += 1
    else:
        if xy[0] > 5:
            pass
        else:
            xy[0] += 1
print(xy)