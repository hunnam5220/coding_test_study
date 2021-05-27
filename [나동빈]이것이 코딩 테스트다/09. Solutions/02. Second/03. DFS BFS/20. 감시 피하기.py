from sys import stdin

n = int(stdin.readline())
board = []

for _ in range(n):
    board.append(list(stdin.readline().rstrip().split()))


def check_move(x, y):
    for i in range(x, len(board)):
        if board[i][y] == 'O':
            break

        if board[i][y] == 'S':
            return False

    for i in range(x, -1, -1):
        if board[i][y] == 'O':
            break

        if board[i][y] == 'S':
            return False

    for i in range(y, len(board)):
        if board[x][i] == 'O':
            break

        if board[x][i] == 'S':
            return False

    for i in range(y, -1, -1):
        if board[x][i] == 'O':
            break

        if board[x][i] == 'S':
            return False

    return True


def check_map():
    for i in range(len(board)):
        for k in range(len(board)):
            if board[i][k] == 'T':
                if not check_move(i, k):
                    return False, 'NO'
    return True, 'YES'


def solution(cnt):
    if cnt == 3:
        chk, result = check_map()
        if chk:
            return result

    else:
        for x in range(n):
            for y in range(n):
                if board[x][y] == 'X':
                    board[x][y] = 'O'
                    cnt += 1
                    if solution(cnt) == 'YES':
                        return 'YES'
                    board[x][y] = 'X'
                    cnt -= 1

    return 'NO'


print(solution(0))