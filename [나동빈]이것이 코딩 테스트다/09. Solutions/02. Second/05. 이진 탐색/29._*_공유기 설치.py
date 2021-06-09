from sys import stdin

n, c = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(stdin.readline()))

arr.sort()

start = 0
end = arr[-1]
result = 0


while start <= end:
    mid = (start + end) // 2
    val = arr[0]
    cnt = 1

    for i in range(1, n):
        if arr[i] >= val + mid:
            val = arr[i]
            cnt += 1

    if cnt >= c:
        start = mid + 1
        result = mid

    else:
        end = mid - 1

print(result)