from collections import deque


def solution(N, stages):
    mother = len(stages)
    stages.sort()

    q = deque(stages)
    fail = 1
    score = [[x, 0] for x in range(N + 1)]

    while q:
        stage = q.popleft()
        if len(q) < 1:
            if stage > N:
                if score[N][1] == 0:
                    fail = 0
                    score[N][0], score[N][1] = N, fail / mother
            else:
                score[stage][0], score[stage][1] = stage, fail / mother
        else:
            if q[0] == stage:
                fail += 1
                continue
            else:
                score[stage][0], score[stage][1] = stage, fail / mother
                mother -= fail
                fail = 1
    score = score[1:]
    score.sort(key=lambda x: (-x[1], x[0]))
    answer = []
    for i in score:
        answer.append(i[0])

    return answer


# [3, 4, 2, 1, 5]
print(solution(5, [2, 1, 2, 5, 5, 6, 2, 4, 3, 3]))

# [4, 1, 2, 3]
print(solution(4, [4, 4, 4, 4, 4]))

N = 5
stages = [1, 2, 2, 1, 3]
print(solution(N, stages))
