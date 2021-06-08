from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()
if n % 2 == 0:
    print(arr[n // 2 - 1])
else:
    print(arr[n // 2])