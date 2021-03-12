from sys import stdin

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
brr = list(map(int, stdin.readline().split()))
arr.sort()
brr.sort(reverse=True)

for step in range(k):
    if arr[step] < brr[step]:
        arr[step], brr[step] = brr[step], arr[step]

print(sum(arr))