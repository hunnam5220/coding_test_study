# 이와 같은 파라메트릭 서치 문제 유형은 재귀함수가 오히려 더 번거로울 수 있음.

from sys import stdin

n, m = map(int, stdin.readline().split())

arr = list(map(int, stdin.readline().split()))
start = 0
end = max(arr)


result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
'''
4 10
19 15 10 17
'''