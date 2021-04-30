def check_board(answer):
    for frame in answer:
        x, y, a = frame
        if a == 0:
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else:
                return False

        elif a == 1:
            if y != 0 and ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:
            answer.append([x, y, a])
            if not check_board(answer):
                answer.pop(answer.index([x, y, a]))

        elif b == 0:
            answer.pop(answer.index([x, y, a]))
            if not check_board(answer):
                answer.append([x, y, a])

    answer.sort()

    return answer


n, build_frame = 5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                     [3, 2, 1, 1]]

print(solution(n, build_frame))


n, build_frame = 5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                     [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

print(solution(n, build_frame))
