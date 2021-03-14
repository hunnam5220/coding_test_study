d = [0] * 1000
d[0], d[1] = 1, 1


for x in range(3, 101):
    d[x] = d[x - 1] + d[x - 2]


print(d[99])
print(d[100])