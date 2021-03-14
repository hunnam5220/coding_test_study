from sys import stdin

n = int(stdin.readline().rstrip())
d = [0] * 300001

d[1] = 1
d[2] = 3


for step in range(3, n + 1):
    d[step] = (d[step - 1] + 2 * d[step - 2]) % 796796

print(d[n])