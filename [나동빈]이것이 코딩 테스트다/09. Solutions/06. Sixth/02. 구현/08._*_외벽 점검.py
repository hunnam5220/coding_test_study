from itertools import permutations


def solution(n, weak, dist):
    weak_length = len(weak)
    answer = len(dist) + 1

    for i in range(weak_length):
        weak.append(weak[i] + n)

    weak.sort()

    for start in range(weak_length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]

            for k in range(start, start + weak_length):
                if weak[k] > position:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[k] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer


# 2
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# 1
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
