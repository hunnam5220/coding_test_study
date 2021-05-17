from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    w_len = len(weak)

    for x in range(w_len):
        weak.append(weak[x] + n)
    weak.sort()

    for start in range(w_len):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]

            for idx in range(start, start + w_len):
                if position < weak[idx]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[idx] + friends[count - 1]

            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer


# 2
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# 1
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
