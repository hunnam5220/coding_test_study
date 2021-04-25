def solution(n, money):
    target = 1
    money.sort()

    for x in money:
        if target < x:
            return target
        target += x


print(solution(5, [3, 2, 1, 1, 9]))
