from collections import deque


def get_next_pos(pos, board):
    # 다음 이동할 위치를 담을 리스트
    next_pos = []

    # 넘겨 받은 위치를 리스트로 변환
    pos = list(pos)

    # 로봇이 위치한 좌표를 1, 2 로 나눔
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 움직일 네 방향
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 네 방향으로 움직이는만큼 반복문 수행
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]

        # 움직일 각 좌표에 0 이 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            # 다음 이동할 위치 리스트에 넣음
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 로봇이 가로로 있다면
    if pos1_x == pos2_x:
        # 각 대각선을 확인
        for i in [-1, 1]:
            # 각 대각선이 0인 경우, 회전 가능한 위치를 다음 이동할 위치 리스트에 넣음
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # 로봇이 세로로 있다면
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    # 위치 리스트를 반환
    return next_pos


def solution(board):
    # 보드를 넘겨받고 보드의 크기를 변수에 저장
    n = len(board)

    # 기존 보드에 테두리를 둘러 새 보드를 생성
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    # 큐 생성
    q = deque()
    # 방문 기록 리스트 생성
    visited = []
    # 초기 위치
    pos = {(1, 1), (1, 2)}

    # 초기 위치와 이동 비용을 큐에 넣음
    q.append((pos, 0))
    # 초기 위치를 방문 기록 리스트에 넣음
    visited.append(pos)

    # 큐가 비어버릴 때까지 진행
    while q:
        # 현재 위치와 이동 비용을 꺼냄
        pos, cost = q.popleft()

        # 현재 위치가 목표인 n, n 위치라면 현재 비용을 리턴
        if (n, n) in pos:
            return cost

        # 다음 위치를 함수를 통해 반환 받아 반복문을 돌림
        for next_pos in get_next_pos(pos, new_board):
            # 다음 이동할 위치가 방문하지 않은 곳이라면,
            if next_pos not in visited:
                # 큐에 방문할 위치와 비용을 넣음
                q.append((next_pos, cost + 1))
                # 방문 처리
                visited.append(next_pos)


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))