from sys import stdin

n, k = map(int, stdin.readline().split())
cnt = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n = n / k
        cnt += 1
    else:
        n -= k
        cnt += 1

print(cnt)