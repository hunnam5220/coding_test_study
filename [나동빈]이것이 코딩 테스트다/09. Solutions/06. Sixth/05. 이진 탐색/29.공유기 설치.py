from sys import stdin


def solution(n, c, arr):

    arr.sort()

    start = 0
    end = arr[-1]
    res = 0

    while start <= end:
        mid = (start + end) // 2
        val = arr[0]
        cnt = 1

        for i in range(n):
            if arr[i] >= val + mid:
                val = arr[i]
                cnt += 1

        if cnt >= c:
            start = mid + 1
            res = mid

        else:
            end = mid - 1

    return res


n, c = map(int, stdin.readline().split())
print(solution(n, c, [int(stdin.readline()) for _ in range(n)]))