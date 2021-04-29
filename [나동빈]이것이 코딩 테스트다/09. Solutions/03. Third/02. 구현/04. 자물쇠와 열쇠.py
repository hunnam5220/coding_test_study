def turn_key(key, key_length):
    new_key = [[0] * key_length for _ in range(key_length)]
    idx = key_length - 1
    for x in range(key_length):
        for y in range(key_length):
            new_key[y][idx] = key[x][y]
            new_key[y][idx] = key[x][y]
            new_key[y][idx] = key[x][y]
        idx -= 1
    return new_key


def check(new_lock, lock_length):
    for x in range(lock_length):
        for y in range(lock_length):
            if new_lock[x + (len(new_lock) // 3)][y + (len(new_lock) // 3)] != 1:
                return False
    return True


def solution(key, lock):
    lock_length = len(lock)
    key_length = len(key)
    new_lock = [[0] * lock_length * 3 for _ in range(lock_length * 3)]

    for x in range(lock_length):
        for y in range(lock_length):
            new_lock[x + (len(new_lock) // 3)][y + (len(new_lock) // 3)] = lock[x][y]

    for turn in range(4):
        key = turn_key(key, key_length)
        for x in range(len(new_lock) - key_length):
            for y in range(len(new_lock) - key_length):
                for x1 in range(key_length):
                    for y1 in range(key_length):
                        new_lock[x + x1][y + y1] += key[x1][y1]

                if check(new_lock, lock_length):
                    return True
                else:
                    for x1 in range(key_length):
                        for y1 in range(key_length):
                            new_lock[x + x1][y + y1] -= key[x1][y1]

    return False


# true
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
