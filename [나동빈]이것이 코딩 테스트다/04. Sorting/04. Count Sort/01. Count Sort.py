arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(arr) + 1)

for step in range(len(arr)):
    count[arr[step]] += 1

for step in range(len(count)):
    for k in range(count[step]):
        print(step, end=' ')