def chk(answer):



def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, oper = frame
        if oper == 0:
            answer.remove([x, y, stuff])
            if not chk()

        else:
            answer.append([x, y, stuff])
            if not chk(answer):
               answer.remove([x, y, stuff])




build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

# build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
# [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

n = 5
print(solution(n, build_frame))
