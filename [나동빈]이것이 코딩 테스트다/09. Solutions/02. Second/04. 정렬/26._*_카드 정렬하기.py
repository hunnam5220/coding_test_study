from sys import stdin

k = 0
arr = []
for _ in range(int(stdin.readline())):
    arr.append(int(stdin.readline()))

n = len(arr)

for i in range(n):
    if i % 2 == 0:
        k += arr[i]
    else:
        k += arr[i]
        if i + 1 != n:
            k += k

print(k)
