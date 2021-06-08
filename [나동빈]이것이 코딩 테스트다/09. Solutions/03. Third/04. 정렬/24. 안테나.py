from sys import stdin
n, arr = int(stdin.readline()), list(map(int, stdin.readline().split()))
arr.sort()
if n % 2 == 0:
    idx = n // 2 - 1
else:
    idx = n // 2
print(arr[idx])