from sys import stdin

arr = []
n = int(stdin.readline())
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))

for i in range(2):
    arr[1][i] += arr[0][0]

test_arr = [item[:] for item in arr]
check_arr = [item[:] for item in arr]

for i in range(1, n - 1):
    for j in range(len(arr[i])):
        for k in [0, 1]:
            if k + j < len(arr[i + 1]):
                test_arr[i + 1][k + j] = max(arr[i][j] + arr[i + 1][k + j], test_arr[i + 1][k + j])

    arr[i + 1] = test_arr[i + 1]


print(max(arr[-1]))
"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""