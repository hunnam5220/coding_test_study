from sys import stdin

arr = list(stdin.readline().rstrip())
calc = ''
step = len(arr)

for x in range(step):
    calc += arr[x]

    if x + 1 != step:
        if arr[x] == '0':
            calc += '+'
        else:
            calc += '*'

print(eval(calc))