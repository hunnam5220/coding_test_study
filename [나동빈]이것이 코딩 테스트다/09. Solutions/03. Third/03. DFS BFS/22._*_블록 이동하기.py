from collections import deque


def turn_ufo():
    pass


def get_next_pos(pos, board):
    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
    next_pos = []
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    for i in range(4):
        n_x1, n_y1, n_x2, n_y2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
        if board[n_x1][n_y1] == 0 and board[n_x2][n_y2] == 0:
            next_pos.append({(n_x1, n_y1), (n_x2, n_y2)})

    if x1 == x2:
        for i in [1, -1]:
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_pos.append({(x1, y1), (x1 + i, y1)})
                next_pos.append({(x2, y2), (x2 + i, y2)})

    if y1 == y2:
        for i in [1, -1]:
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append({(x1, y1), (x1, y1 + i)})
                next_pos.append({(x2, y2), (x2, y2 + i)})

    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for x in range(n):
        for y in range(n):
            new_board[x + 1][y + 1] = board[x][y]

    q = deque()
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited = [pos]

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost

        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board=board))
