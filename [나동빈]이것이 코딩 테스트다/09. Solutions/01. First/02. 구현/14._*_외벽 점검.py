from itertools import permutations


def solution(n, weak, dist):
    leng = len(weak)
    for x in range(leng):
        weak.append(weak[x] + n)

    answer = len(dist) + 1

    for start in range(leng):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]

            for index in range(start, start + leng):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1

    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
# 2
print(solution(n, weak, dist))


n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

# 1
print(solution(n, weak, dist))