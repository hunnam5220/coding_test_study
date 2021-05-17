def check_lock(new_lock, lock_length):
    for x in range(lock_length):
        for y in range(lock_length):
            if new_lock[x + lock_length][y + lock_length] != 1:
                return False
    return True


def turn_key(key, key_length):
    new_key = [[0] * key_length for _ in range(key_length)]
    for x in range(key_length):
        for y in range(key_length):
            new_key[y][key_length - 1 - x] = key[x][y]

    return new_key


def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)

    new_lock = [[0] * lock_length * 3 for _ in range(lock_length * 3)]
    for x in range(lock_length):
        for y in range(lock_length):
            new_lock[x + lock_length][y + lock_length] = lock[x][y]

    for _ in range(4):
        key = turn_key(key, key_length)

        for x in range(len(new_lock) - key_length):
            for y in range(len(new_lock) - key_length):
                for i in range(key_length):
                    for j in range(key_length):
                        new_lock[x + i][y + j] += key[i][j]

                if check_lock(new_lock, lock_length):
                    return True
                else:
                    for i in range(key_length):
                        for j in range(key_length):
                            new_lock[x + i][y + j] -= key[i][j]

    return False


# true
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
