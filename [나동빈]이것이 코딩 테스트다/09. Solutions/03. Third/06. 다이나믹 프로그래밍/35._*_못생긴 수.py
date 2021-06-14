from sys import stdin

n = int(stdin.readline())

u = [0] * n
u[0] = 1

i2, i3, i5 = 0, 0, 0

n2, n3, n5 = 2, 3, 5

for i in range(1, n):
    u[i] = min(n2, n3, n5)

    if u[i] == n2:
        i2 += 1
        n2 = u[i2] * 2

    if u[i] == n3:
        i3 += 1
        n3 = u[i3] * 3

    if u[i] == n5:
        i5 += 1
        n5 = u[i5] * 5


print(u[n - 1])