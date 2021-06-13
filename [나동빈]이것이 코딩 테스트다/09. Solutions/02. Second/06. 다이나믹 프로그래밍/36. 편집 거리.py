from sys import stdin

_1 = stdin.readline().rstrip()
_2 = stdin.readline().rstrip()

res = 0

for i in range(len(_1)):
    tmp = False
    dist = 0
    for j in range(len(_2)):
        if _1[i] == _2[j]:
            tmp = True
            dist = abs(i - j)
            break

    if tmp and dist > 0:
        res += dist

print(res)