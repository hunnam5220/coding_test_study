from sys import stdin

string = list(stdin.readline().rstrip())
c = [False, False]
result = 1e9

for x in range(2):
    cnt = 0
    for s in string:
        if int(s) == x and not c[x]:
            c[x] = True
            cnt += 1
        elif int(s) != x and c[x]:
            c[x] = False
    result = min(result, cnt)


print(result)

"""
0001100
"""