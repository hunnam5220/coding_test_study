arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for step in range(len(arr)):
    min_idx = step

    for j in range(step + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j

    arr[step], arr[min_idx] = arr[min_idx], arr[step]

print(arr)