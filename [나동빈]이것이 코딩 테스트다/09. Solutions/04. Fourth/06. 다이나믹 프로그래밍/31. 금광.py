from sys import stdin

for _ in range(int(stdin.readline())):
    arr = []
    r, c = map(int, stdin.readline().split())
    data = list(map(int, stdin.readline().split()))
    result = 0

    for i in range(r):
        arr.append(data[i * c:(i + 1) * c])

    test_arr = [item[:] for item in arr]
    for i in range(1, c):
        for j in range(r):
            for k in [-1, 0, 1]:
                if 0 <= k + j < r:
                    test_arr[j + k][i] = max(test_arr[j + k][i], arr[j + k][i] + arr[j][i - 1])

        for j in range(r):
            arr[j][i] = test_arr[j][i]

    for i in range(r):
        result = max(arr[i][-1], result)

    print(result)



"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""