from sys import stdin

n = int(stdin.readline().rstrip())
arr = []
for step in range(n):
    arr.append(list(stdin.readline().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_t(i, k):
    """ T 바로 옆 위 아래에 학생있으면 무조건 NO """

    for o in range(4):
        for p in range(1, n):
            nx = i + dx[o] * p
            ny = k + dy[o] * p

            if -1 < nx < n and -1 < ny < n:
                if arr[nx][ny] == 'S':
                    return False
                if arr[nx][ny] == 'O':
                    return True

    return True


def inst(count):
    if count == 3:
        for i in range(n):
            for k in range(n):
                if arr[i][k] == 'T':
                    if not find_t(i, k):
                        return

    for x in range(n):
        for y in range(n):
            if arr[x][y] == 'X':
                arr[x][y] = 'O'
                count += 1
                inst(count)
                arr[x][y] = 'X'
                count -= 1


inst(0)