from sys import stdin


def dfs(k, j, idx):
    if k >= n or j >= n or k < 0 or j < 0:
        return False

    if arr[k][j] == 9:
        return False

    if arr[k][j] != 0:
        if check_apple(k, j):
            if idx == 0:
                arr[k][j - 1] = 9

            elif idx == 1:
                arr[k - 1][j] = 9

            elif idx == 2:
                arr[k + 1][j] = 9

            else:
                arr[k][j + 1] = 9
        else:
            if idx == 0:
                arr[k][j - 1] = 0

            elif idx == 1:
                arr[k - 1][j] = 0

            elif idx == 2:
                arr[k + 1][j] = 0

            else:
                arr[k][j + 1] = 0

        arr[k][j] = 9

        return True

    return True


def check_apple(k, j):
    if arr[k][j] == 1:
        return True
    return False


n = int(stdin.readline().rstrip())
arr = [[0] * n for _ in range(n)]
global k, j
k, j = 0, 0
c, chk = '', True
time, idx = 0, 0

for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().split())
    arr[a - 1][b - 1] = 1

for step in range(int(stdin.readline().rstrip())):
    x, c = stdin.readline().split()
    for k in range(int(x)):
        if chk:
            if idx == 0:
                j += 1
            elif idx == 1:
                k += 1
            elif idx == 2:
                k -= 1
            else:
                j -= 1

            time += 1
            chk = dfs(k, j, idx)
            if not chk:
                print(time)
                break

    if c == 'D':
        idx += 1
        if idx >= 4:
            idx = 0
    else:
        idx -= 1
        if idx <= -1:
            idx = 3





"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
>> 9

10
4
1 2
1 3
1 4
1 5
4 
8 D
10 D
11 D
13 L
>> 21

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
>> 13
"""