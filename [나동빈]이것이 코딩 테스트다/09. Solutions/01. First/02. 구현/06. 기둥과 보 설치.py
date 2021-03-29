def solution(n, build_frame):

    arr = [[9] * (n + 1) for _ in range(n + 1)]
    for x, y, g, i in build_frame:
        if i == 1:
            if g == 0:
                arr[n - y][n - x] = 0
            else:
                arr[n - y][n - x] = 1
        else:
            arr[n - y][n - x] = 9

    return arr


# [x, y, (0,1), (0, 1)]
# 좌표 좌표 기둥, 보 삭제 설치


build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

# arr = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
#        [1, 1, 1, 0], [2, 2, 0, 1]]
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
n = 5
array = solution(n, build_frame)
array.reverse()
result = []

print(array)

for x in range(n):
    for y in range(n):
        if array[x][y] == 0:
            result.append([x, y, 0])
        else:
            result.append([x, y, 1])

print(result)