def binary(arr, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if mid == arr[mid]:
        return mid

    elif arr[mid] > mid:
        return binary(arr, start, mid - 1)
    else:
        return binary(arr, mid + 1, end)


def solution(n, arr):
    start = 0
    end = n

    idx = binary(arr, start, end)

    if idx is None:
        return -1
    else:
        return idx


n = 5
print(solution(n, arr))

n = 7
arr = [-15, -4, 2, 8, 9, 13, 15]
print(solution(n, arr))

n = 7
arr = [-15, -4, 3, 8, 9, 13, 15]
print(solution(n, arr))