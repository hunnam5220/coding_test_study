def rotation_key(key, m):
    new_key = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            new_key[j][m - 1 - i] = key[i][j]

    return new_key


def check(c_lock):
    x = len(c_lock) // 3

    for i in range(x, x * 2):
        for j in range(x, x * 2):
            if c_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock[0])
    m = len(key[0])
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                new_lock[i + n][j + n] = 1

    for zxc in range(4):
        key = rotation_key(key, m)

        for z in range(1, len(new_lock) - n):
            for k in range(1, len(new_lock) - n):
                c_lock = [item[:] for item in new_lock]

                for i in range(m):
                    for j in range(m):
                        c_lock[i + z][j + k] += key[i][j]

                if check(c_lock):
                    return True

    return False


# key = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# lock = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(solution(key, lock))

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))



"""
1 23 ~ 33
"""