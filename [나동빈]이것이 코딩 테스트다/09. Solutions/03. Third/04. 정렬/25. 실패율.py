from collections import deque


def solution(N, stages):
    mother = len(stages)
    k = [[x, 0] for x in range(N + 1)]
    stages.sort()
    q = deque(stages)
    fail = 1

    while q:
        stage = q.popleft()
        if len(q) < 1:
            if stage > N:
                if k[N][1] == 0:
                    fail = 0
                    k[N][1] = fail / mother
            else:
                k[stage][1] = fail / mother

        else:
            if stage == q[0]:
                fail += 1
                continue

            else:
                k[stage][1] = fail / mother
                mother -= fail
                fail = 1
    k = k[1:]
    k.sort(key=lambda x: (-x[1], x[0]))
    answer = []
    for i in k:
        answer.append(i[0])

    return answer


# [3 ,4 ,2 ,1 ,5]
N = 5
stages = [2, 1, 2, 4, 4, 4, 2, 4, 3, 3]
print(solution(N, stages))

# [4 ,1 ,2 ,3]
# N = 4
# stages = [4 ,4 ,4 ,4 ,4]
# print(solution(N, stages))
