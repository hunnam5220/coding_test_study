from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)

    for i in range(len(weak)):
        weak.append(weak[i] + n)
    weak.sort()
    answer = len(dist) + 1
    dist.sort(reverse=True)

    for start in range(weak_len):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]

            for idx in range(start, start + weak_len):
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

# 3
print(solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))

# 2
print(solution(200, [0, 100], [1, 1]))
