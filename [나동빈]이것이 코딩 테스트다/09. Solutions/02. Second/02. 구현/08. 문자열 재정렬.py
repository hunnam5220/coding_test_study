from sys import stdin

arr = list(stdin.readline().rstrip())

arr.sort()
s = 0
for i in range(len(arr)):
    if arr[i].isdigit():
        s += int(arr[i])
    else:
        arr = arr[i:]
        arr.append(str(s))
        print(''.join(arr))
        break



"""
K1KA5CB7

AJKDLSI412K4JSJ9D
"""