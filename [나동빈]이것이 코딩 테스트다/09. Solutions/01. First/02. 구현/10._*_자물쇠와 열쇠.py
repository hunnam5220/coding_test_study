def solution(key, lock):
    """ Main Function """

    """  """
    n = len(lock)
    """  """
    m = len(key)

    """ 자물솨 크기의 세 배의 새 자물쇠 생성 """
    gear_third_lock = [[0] * (n * 3) for _ in range(n * 3)]

    """ 새로운 자물쇠 중간에 기존 자물쇠 집어 넣기"""
    for x in range(n):
        for y in range(n):
            gear_third_lock[x + n][y + n] = lock[x][y]

    """ 90도씩 4번 회전 """
    for step in range(4):
        """ 90도 회전 """
        key = rotate_a_matrix_by_90_degree(key)

        """ 키우는건 세 배, 이동할 수 있는 거리는 3 - 1배 """
        for x in range(n * 2):
            for y in range(n * 2):

                """ 열쇠를 자물쇠 부분에 더함 """
                for i in range(m):
                    for j in range(m):
                        gear_third_lock[x + i][y + j] += key[i][j]

                """ 자물쇠 부분이 모두 1인지 검사 """
                if check(gear_third_lock):
                    return True

                """ True return 안됐으니까 다시 원상복구 함 """
                for i in range(m):
                    for j in range(m):
                        gear_third_lock[x + i][y + j] -= key[i][j]

    return False


def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]

    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res


def check(lock):
    r = len(lock) // 3

    for x in range(r, r * 2):
        for y in range(r, r * 2):
            if lock[x][y] != 1:
                return False
    return True


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

if solution(key, lock):
    print('true')
else:
    print('false')