from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))


def find_num(arr, a, b):
    mid = (a + b) // 2
    if mid == 0:
        return -1
    if mid == arr[mid]:
        return mid

    if arr[mid] > mid:
        return find_num(arr, a, mid - 1)
    else:
        return find_num(arr, mid + 1, b)


print(find_num(arr, 0, n - 1))

"""
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 4 3 8 9 13 15

"""