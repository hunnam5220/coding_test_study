from sys import stdin

s = list(map(int, stdin.readline().rstrip()))
arr = [0, 0]
chk = s[0]

if chk:
    arr[1] += 1
else:
    arr[0] += 1

for i in range(1, len(s)):
    if s[i] == chk:
        continue
    else:
        if chk:
            chk = 0
        else:
            chk = 1
        arr[chk] += 1

print(min(arr))
"""
0001100
1010110011
"""