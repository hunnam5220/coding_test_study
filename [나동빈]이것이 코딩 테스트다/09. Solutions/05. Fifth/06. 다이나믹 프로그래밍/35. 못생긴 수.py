from sys import stdin


def solution(n):
    ugly = [1]

    i2, i3, i5 = 0, 0, 0
    n2, n3, n5 = 2, 3, 5

    for _ in range(n):
        k = min(n2, n3, n5)
        ugly.append(k)
        if k == n2:
            i2 += 1
            n2 = ugly[i2] * 2

        if k == n3:
            i3 += 1
            n3 = ugly[i3] * 3

        if k == n5:
            i5 += 1

    return ugly[n - 1]


print(solution(int(stdin.readline())))