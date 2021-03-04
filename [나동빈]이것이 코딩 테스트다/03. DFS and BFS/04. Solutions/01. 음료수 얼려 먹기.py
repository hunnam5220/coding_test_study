from sys import stdin


n, m = map(int, stdin.readline().rstrip().split())
arr = []

for step in range(n):
    arr.append(list(map(int, stdin.readline().rstrip())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False


result = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y):
            result += 1

print(result)

'''
4 5
00110
00011
11111
00000
'''