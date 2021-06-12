from sys import stdin

n = int(stdin.readline())

arr = []

for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

for i in range(2):
    arr[1][i] += arr[0][0]

test_arr = [item[:] for item in arr]

for i in range(1, n - 1):
    for j in range(len(arr[i])):
        num = arr[i][j]
        for k in [0, 1]:
            if -1 < j + k < len(arr[i + 1]):
                test_arr[i + 1][j + k] = max(test_arr[i + 1][j + k], arr[i + 1][j + k] + num)

    arr[i + 1] = test_arr[i + 1]

print(max(arr[-1]))