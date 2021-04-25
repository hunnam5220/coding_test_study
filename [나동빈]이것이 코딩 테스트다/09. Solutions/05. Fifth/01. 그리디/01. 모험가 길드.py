def solution(n, arr):
    result = 0
    cnt = 0
    arr.sort()
    for x in arr:
        cnt += 1
        if x == cnt:
            cnt = 0
            result += 1

    return result


print(solution(5, [2, 3, 1, 2, 2]))
print(solution(6, [2, 4, 1, 1, 1]))