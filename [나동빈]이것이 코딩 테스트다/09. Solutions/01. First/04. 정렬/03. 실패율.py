def solution(n, stages):
    k = len(stages)
    stages.sort()
    calc = [[0, x + 1] for _, x in zip(range(n), range(n))]
    for i in stages:
        if i <= n:
            calc[i - 1][0] += 1

    for p in range(n):
        tmp = calc[p][0]
        if calc[p][0] != 0:
            calc[p][0] /= k
        else:
            calc[p][0] = 0
        k -= tmp

    calc.sort(key=lambda x: (-x[0], x[1]))
    answer = []

    for step in calc:
        answer.append(step[1])

    return answer


n, stages = 5, [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))

n, stages = 4, [1, 1, 1, 1, 1]
print(solution(n, stages))

n, stages = 4, [4, 4, 4, 4, 4]
print(solution(n, stages))

n, stages = 4, [5, 3, 4, 4, 4]
print(solution(n, stages))

n, stages = 2, [3, 3, 2, 1, 1]
print(solution(n, stages))

n, stages = 4, [1, 1, 1, 1, 1]
print(solution(n, stages))