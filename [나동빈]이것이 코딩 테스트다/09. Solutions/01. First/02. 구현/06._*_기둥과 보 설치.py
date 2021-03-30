def chk(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer or [x, y, 1] in answer:
                continue
            return False

        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False

    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, oper = frame
        if oper == 0:
            answer.remove([x, y, stuff])
            if not chk(answer):
                answer.append([x, y, stuff])

        else:
            answer.append([x, y, stuff])
            if not chk(answer):
               answer.remove([x, y, stuff])

    return sorted(answer)




n = 5
# build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
# print(solution(n, build_frame))

build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
[2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
print(solution(n, build_frame))
