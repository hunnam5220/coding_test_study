from sys import stdin


def recursive_func(n):
    if n == 1:
        return n
    return recursive_func(n - 1) * n


def iterative_func(n):
    result = 1
    for step in range(1, n+1):
        result *= step
    return result


n = int(stdin.readline().rstrip())
print(recursive_func(n))
print(iterative_func(n))
