from sys import stdin

arr = list(map(int, list(stdin.readline().rstrip())))
idx = len(arr) // 2

if sum(arr[:idx]) == sum(arr[idx:]):
    print("LUCKY")
else:
    print("READY")