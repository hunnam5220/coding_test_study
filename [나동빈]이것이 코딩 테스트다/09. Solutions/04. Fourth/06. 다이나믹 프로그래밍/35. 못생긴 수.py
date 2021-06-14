from sys import stdin

n = int(stdin.readline())

u = [1]

i2, i3, i5 = 0, 0, 0
n2, n3, n5 = 2, 3, 5

for _ in range(n):
    k = min(n2, n3, n5)
    u.append(k)

    print(k)

    if k == n2:
        i2 += 1
        n2 = u[i2] * 2

    if k == n3:
        i3 += 1
        n3 = u[i3] * 3

    if k == n5:
        i5 += 1
        n5 = u[i5] * 5

print(u[n - 1])