from sys import stdin


def sequentail_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1


input_data = stdin.readline().split()
n = int(input_data[0])
target = input_data[1]

array = ['Hanul', 'Jonggu', 'Dongbin', 'Taeil', 'SangWook']

print(sequentail_search(n, target, array))
