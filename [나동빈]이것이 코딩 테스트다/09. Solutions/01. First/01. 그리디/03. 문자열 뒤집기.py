from sys import stdin

string = list(stdin.readline().rstrip())
arr = [0, 0]
chk = ''

for x in string:
    if x == '0' and chk != '0':
        chk = '0'
        arr[0] += 1
    elif x == '1' and chk != '1':
        chk = '1'
        arr[1] += 1

if arr[0] > arr[1]:
    print(arr[1])
else:
    print(arr[0])