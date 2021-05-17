from itertools import permutations


def solution(n, weak, dist):
    new_weak = []
    for i in weak:
        new_weak.extend([i, i + n])

    answer = len(dist) + 1

    new_weak = list(set(new_weak))
    new_weak.sort()

    new_dists = list(permutations(dist, len(dist)))

    for start in range(len(weak)):
        for friends in new_dists:
            count = 1

            position = new_weak[start] + friends[count - 1]

            for idx in range(start, start + len(weak)):
                if position < new_weak[idx]:
                    count += 1
                    if count > len(dist):
                        break
                    position = new_weak[idx] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1

    return answer


# 2
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))

# 1
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))