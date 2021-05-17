from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    answer = len(dist) + 1

    # 원형을 쭉 펴서 일자 형태로 만들어준다.
    for x in range(length):
        weak.append(weak[x] + n)

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1

            # 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]

            # 시작점부터 취약한 지점을 weak의 길이만큼 점검
            for index in range(start, start + length):
                # 점검할 수 있는 마지막지점보다 취약한 지점이 클 경우

                if position < weak[index]:
                    # 친구 한명 더 소환
                    count += 1

                    # 친구를 불러낸 수가 총 친구 수를 넘었을 때
                    if count > len(dist):
                        break

                    # 한명더 소환한 친구가 점검할 수 있는 마지막 위치
                    position = weak[index] + friends[count - 1]

            # 친구 소환 횟수와 answer 비교해서 작은 값 넣기
            answer = min(answer, count)

    # 친구 다 모였는데도 취약점 점검 안되면 -1 반환
    if answer > len(dist):
        return -1

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
