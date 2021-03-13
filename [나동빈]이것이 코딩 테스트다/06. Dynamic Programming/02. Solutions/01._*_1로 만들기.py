from sys import stdin

n = int(stdin.readline().rstrip())
d = [0] * 10000

for step in range(2, n + 1):
    d[step] = d[step - 1] + 1

    if step % 2 == 0:
        d[step] = min(d[step], d[step // 2] + 1)

    if step % 3 == 0:
        d[step] = min(d[step], d[step // 3] + 1)

    if step % 5 == 0:
        d[step] = min(d[step], d[step // 5] + 1)

print(d[n])