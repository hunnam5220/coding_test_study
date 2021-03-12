"""
5
8 3 7 9 2
3
5 7 9
"""

from sys import stdin

n = int(stdin.readline().rstrip())
store = list(map(int, stdin.readline().split()))

m = int(stdin.readline().rstrip())
customer = list(map(int, stdin.readline().split()))


def binary_search(target, store):
    mid = len(store) // 2

    if store[mid] == target:
        return 'yes'

    elif len(store) == 1:
        return 'no'

    elif store[mid] > target:
        return binary_search(target, store[:mid])

    else:
        return binary_search(target, store[mid:])


store.sort()
for target in customer:
    print(binary_search(target, store), end=' ')