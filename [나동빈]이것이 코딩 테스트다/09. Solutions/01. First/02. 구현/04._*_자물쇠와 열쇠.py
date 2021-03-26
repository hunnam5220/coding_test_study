def solution(key, lock):
    n = len(lock)
    m = len(key)
    gear_third_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for x in range(n):
        for y in range(n):
            gear_third_lock[x + n][y + n] = lock[x][y]

    for step in range(4):
        key = rotate_a_matrix_by_90_degree(key)

        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        gear_third_lock[x + i][y + j] += key[i][j]

                if check(gear_third_lock):
                    return True

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