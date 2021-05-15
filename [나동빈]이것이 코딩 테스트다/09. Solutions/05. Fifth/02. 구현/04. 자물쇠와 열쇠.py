def chk_unlock(new_lock, lock_length):
    for i in range(lock_length):
        for j in range(lock_length):
            if new_lock[i + lock_length][j + lock_length] != 1:
                return False
    return True


def turn_key(key, key_length):
    new_key = [[0] * key_length for _ in range(key_length)]

    for i in range(key_length):
        for j in range(key_length):
            new_key[j][key_length - 1 - i] = key[i][j]
            new_key[j][key_length - 1 - i] = key[i][j]
            new_key[j][key_length - 1 - i] = key[i][j]

    return new_key


def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)

    new_lock = [[0] * lock_length * 3 for _ in range(lock_length * 3)]

    for i in range(lock_length):
        for j in range(lock_length):
            new_lock[i + lock_length][j + lock_length] = lock[i][j]

    for _ in range(4):
        key = turn_key(key, key_length)

        for x in range(len(new_lock) - key_length):
            for y in range(len(new_lock) - key_length):

                for kx in range(key_length):
                    for ky in range(key_length):
                        new_lock[x + kx][y + ky] += key[kx][ky]

                if chk_unlock(new_lock, lock_length):
                    return True

                else:
                    for kx in range(key_length):
                        for ky in range(key_length):
                            new_lock[x + kx][y + ky] -= key[kx][ky]
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
