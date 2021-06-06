from sys import stdin

n = int(stdin.readline())
board = []
tc = []
for i in range(n):
    data = list(stdin.readline().split())
    board.append(data)
    for j in range(n):
        if data[j] == 'T':
            tc.append((i, j))


def check(t, board):
    x, y = t

    for a in range(x + 1, n):
        if board[a][y] == 'O':
            break

        if board[a][y] == 'S':
            return False

    for b in range(y + 1, n):
        if board[x][b] == 'O':
            break

        if board[x][b] == 'S':
            return False

    for c in range(x - 1, -1, -1):
        if board[c][y] == 'O':
            break
        if board[c][y] == 'S':
            return False

    for d in range(y - 1, -1, -1):
        if board[x][d] == 'O':
            break
        if board[x][d] == 'S':
            return False

    return True


def solutions(cnt):
    if cnt == 3:
        for t in tc:
            if not check(t, board):
                return False

        return True

    else:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    board[i][j] = 'O'
                    cnt += 1
                    if solutions(cnt):
                        return True
                    board[i][j] = 'X'
                    cnt -= 1
        return False


if solutions(0):
    print('YES')
else:
    print('NO')
