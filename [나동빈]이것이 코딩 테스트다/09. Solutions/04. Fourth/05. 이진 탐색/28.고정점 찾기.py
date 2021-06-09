from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))


def binary(arr, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid

    elif arr[mid] < mid:
        return binary(arr, mid + 1, end)

    else:
        return binary(arr, start, mid - 1)


idx = binary(arr, 0, n)

if idx is None:
    print(-1)
else:
    print(idx)