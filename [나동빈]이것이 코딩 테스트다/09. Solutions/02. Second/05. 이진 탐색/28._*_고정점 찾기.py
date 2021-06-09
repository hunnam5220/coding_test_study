from sys import stdin


def binary_search(arr, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid

    elif arr[mid] > mid:
        return binary_search(arr, start, mid - 1)

    else:
        return binary_search(arr, mid + 1, end)


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

idx = binary_search(arr, 0, n - 1)
if idx is None:
    print(-1)
else:
    print(idx)



"""
# 3
5
-15 -6 1 3 7

# 2
7
-15 -4 2 8 9 13 15

# -1
7
-15 -4 3 8 9 13 15
"""
