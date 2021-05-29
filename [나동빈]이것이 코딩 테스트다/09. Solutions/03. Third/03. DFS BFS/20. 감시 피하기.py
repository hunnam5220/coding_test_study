from sys import stdin

n = int(stdin.readline())
board = []
teachers = []

for i in range(n):
    data = list(stdin.readline().split())
    board.append(data)
    for j in range(len(data)):
        if board[i][j] == 'T':
            teachers.append((i, j))


def check(x, y):
    for a in range(x + 1, len(board)):
        if board[a][y] == 'O':
            break

        if board[a][y] == 'S':
            return False

    for b in range(x - 1, -1, -1):
        if board[b][y] == 'O':
            break

        if board[b][y] == 'S':
            return False

    for c in range(y + 1, len(board)):
        if board[x][c] == 'O':
            break

        if board[x][c] == 'S':
            return False

    for d in range(y - 1, -1, -1):
        if board[x][d] == 'O':
            break

        if board[x][d] == 'S':
            return False

    return True


def check_map():
    for teacher in teachers:
        x, y = teacher
        if not check(x, y):
            return False
    return True


def solution(cnt):
    if cnt == 3:
        if check_map():
            return True

    else:
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 'X':
                    board[x][y] = 'O'
                    cnt += 1
                    if solution(cnt):
                        return True
                    board[x][y] = 'X'
                    cnt -= 1
    return False


if not solution(0):
    print('NO')
else:
    print('YES')
